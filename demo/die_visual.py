from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

d6 = Die()

# 随机掷骰子
results = []
for roll_num in range(1000):
    result = d6.roll()
    results.append(result)

# 统计骰子每个面出现的次数
frequencies = []
for value in range(1, d6.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 绘制直方图
# 点数
x_values = list(range(1, d6.num_sides + 1))
# Bar()用来绘制条形图,这个类必须放在[]中
data = [Bar(x=x_values, y=frequencies)]
# x轴的标题
x_axis_config = {'title': '结果'}
# y轴的标题
y_axis_config = {'title': '频率'}
# 直方图的标题和x, y轴的数据
my_layout = Layout(title='掷一个D6 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
# 生成图表
# offline.plot()需要一个包含数据和布局对象的字典，还接受一个文件名，指定要将图表保存到哪里。
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
