import numpy as np
import matplotlib.pyplot as plt


X = np.arange(-1, 1, 0.003)
Y = X * np.sin(1 / X)
plt.plot(X, Y)
plt.plot(X, X, '--k')
plt.plot(X, -X, '--k')

X = np.asarray([2 / (i * np.pi) for i in range(1, 10)] + [-2 / (i * np.pi) for i in range(1, 10)])
Y = X * np.sin(1 / X)
plt.plot(X, Y, 'ro')

plt.show()

#sin(1 / x)
# x sin(1 / x)
