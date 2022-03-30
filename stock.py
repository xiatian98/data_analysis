import backtrader as bt
import akshare as ak
import pandas as pd
from datetime import datetime


# 创建策略继承bt.Strategy
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        # 记录策略的执行日志
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # 保存收盘价的引用
        self.dataclose = self.datas[0].close
        # 跟踪挂单
        self.order = None

    # 策略代码
    def next(self):
        # 月初定投 1000元
        # 获取当前股价
        if self.datas[0].datetime.date(0).day == 1:
            # 跟踪订单避免重复
            self.order = self.buy(size=int(1000 / self.dataclose[0]))

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # broker 提交/接受了，买/卖订单则什么都不做
            return

        # 检查一个订单是否完成
        # 注意: 当资金不足时，broker会拒绝订单
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('已买入{0}股, 交易价格{1}'.format(order.executed.size, order.executed.price))
            elif order.issell():
                self.log('已卖出{0}股, 交易价格{1}'.format(order.executed.size, order.executed.price))

            # 记录当前交易数量
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('订单取消/保证金不足/拒绝')

        # 其他状态记录为：无挂起订单
        self.order = None


def get_data(code, start, end):
    df = ak.fund_etf_hist_sina(symbol=code)
    df['date'] = pd.to_datetime(df['date'])
    df = df[(df.date > start.strftime("%Y-%m-%d")) & (df.date < end.strftime("%Y-%m-%d"))]
    # 处理字段命名，以符合 Backtrader 的要求
    df.columns = [
        'date',
        'open',
        'close',
        'high',
        'low',
        'volume',
    ]
    # 把 date 作为日期索引，以符合 Backtrader 的要求
    df.index = pd.to_datetime(df['date'])
    return df


if __name__ == '__main__':
    # 创建Cerebro引擎
    print('\n')
    cerebro = bt.Cerebro()

    # 为Cerebro引擎添加策略
    cerebro.addstrategy(TestStrategy)

    # Cerebro引擎在后台创建broker(经纪人)，系统默认资金量为10000
    # 设置投资金额600000.0
    cerebro.broker.setcash(60000.0)

    start_date = datetime(2016, 8, 22)  # 回测开始时间
    end_date = datetime(2021, 8, 22)  # 回测结束时间
    data = bt.feeds.PandasData(dataname=get_data('sh510300', start_date, end_date), fromdate=start_date,
                               todate=end_date)  # 加载数据

    # 加载交易数据
    cerebro.adddata(data)

    # 设置佣金为0.001,除以100去掉%号
    cerebro.broker.setcommission(commission=0.001)

    # 引擎运行前打印期出资金
    print('组合期初资金: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    # 引擎运行后打期末资金
    print('组合期末资金: %.2f' % cerebro.broker.getvalue())

    # 绘制图像
    cerebro.plot()
