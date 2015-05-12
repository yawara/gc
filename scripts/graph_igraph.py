import igraph
from matplotlib import pyplot as plt
import numpy as np
import itertools

n=8
degrees = np.array([3 for i in range(8)])

for p in itertools.product((0,1),repeat=int(n*(n-1)/2)):
  if degrees.sum() == np.array(p).sum() * 2:  
    M = [ [ 0 for i in range(n) ] for i in range(n) ]
    q = 0

    for i in range(n):
      for j in range(n):
        if i < j:
          M[i][j], M[j][i] = p[q], p[q]
          q+=1
    
    np_M = np.array(M) 
    ds = np.sum(np_M,axis=0)

    if np.all(ds == degrees):
      G = igraph.Graph.Adjacency(M)
      if G.is_connected():
        if G.diameter() <= 2:
          print(M)
          #igraph.plot(G)
          break
      
print("not found")