import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('tableau-colorblind10')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)
ax.set_title("SQUARES", fontsize=14)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("X^2", fontsize=14)
ax.axis([0, 1100, 0, 1100000])
plt.show()
