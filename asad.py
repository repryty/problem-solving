from matplotlib import pyplot as plt

y = [(-2)**(i-50) for i in range(100)]

plt.plot([i-50 for i in range(100)], y)

plt.show()