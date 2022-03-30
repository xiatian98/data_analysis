from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die(10)

# 随机掷骰子
results = []
for roll_num in range(5_0000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 统计骰子每个面出现的次数
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 绘制直方图
# 点数
x_values = list(range(2, max_result + 1))
# Bar()用来绘制条形图,这个类必须放在[]中
data = [Bar(x=x_values, y=frequencies)]
# x轴的标题
x_axis_config = {'title': '掷骰子的结果', 'dtick': 1}
# y轴的标题
y_axis_config = {'title': '每个面出现的频率'}
# 直方图的标题和x, y轴的数据
my_layout = Layout(title='掷1个D6和1个D10 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
# 生成图表
# offline.plot()需要一个包含数据和布局对象的字典，还接受一个文件名，指定要将图表保存到哪里。
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
