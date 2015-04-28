import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import itertools

n=9

for p in itertools.product((0,1),repeat=int(n*(n-1)/2)):
  M = np.zeros((n,n))
  q = 0
  
  for i in range(n):
    for j in range(n):
      if i < j:
        M[i][j], M[j][i] = p[q], p[q]
        q+=1
      
  ds = np.sum(M,axis=0)
  degrees = [4] + [ 3 for i in range(8) ]
  if np.all(ds == np.array(degrees)):
    G = nx.from_numpy_matrix(M)
    if nx.is_connected(G):
      if nx.diameter(G) <= 2:
        print(M)
        nx.draw(G)
        plt.show()
        break
      
print("not found")