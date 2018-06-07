import numpy as np
from numpy import pi, sin, cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

if __name__ == '__main__':
  n = 10
  theta, phi = np.meshgrid(np.linspace(0,pi,n),np.linspace(0,2*pi,n))

  X = 3 * sin(theta) * cos(phi)
  Y = 2 * sin(theta) * sin(phi)
  Z = cos(theta)

  print(X,Y,Z)
  
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_wireframe(X,Y,Z)
  plt.show()
  fig.savefig("answer_9_1_a.eps")
