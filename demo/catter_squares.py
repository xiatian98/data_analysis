import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
ax.set_title("SQUARES", fontsize=24)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("X^2", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()