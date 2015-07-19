import numpy as np
from numpy import pi, sin, cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

if __name__ == '__main__':
  n,m = 50,20
  t, s = np.meshgrid(np.linspace(0,2*pi,n),np.linspace(0,1,m))

  X = s * cos(t)
  Y = s * sin(t)
  Z = s

  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_wireframe(X,Y,Z)
  plt.show()
  fig.savefig("answer_8_3_a.eps")
