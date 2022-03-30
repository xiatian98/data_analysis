import matplotlib.pyplot as plt
"""
可以使用的颜色
['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 
'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 
'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 
'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 
'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 
'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 
'seaborn-whitegrid', 'tableau-colorblind10']
"""
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.set_title("SQUARES", fontsize=24)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("X^2", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()
