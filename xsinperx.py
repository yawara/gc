import numpy as np
import matplotlib.pyplot as plt


X = np.arange(-1, 1, 0.003)
Y = X * np.sin(1 / X)

plt.plot(X, Y)
plt.plot(X, X)
plt.plot(X, -X)
plt.show()

#sin(1 / x)
# x sin(1 / x)
