import numpy as np
import matplotlib.pyplot as plt


X = np.arange(-1, 1, 0.003)
Y = np.sin(1 / X)
plt.plot(X, Y)
X = np.asarray([2 / (i * np.pi) for i in range(1, 10)] + [-2 / (i * np.pi) for i in range(1, 10)])
Y = np.sin(1 / X)
plt.plot(X, Y, 'ro')
plt.ylim([-1.1, 1.1])
plt.show()

#sin(1 / x)
# x sin(1 / x)
