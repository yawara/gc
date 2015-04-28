import networkx as nx
from matplotlib import pyplot as plt
import scipy as sp
import itertools

n=6
degrees = sp.array([3 for i in range(2)]+[2 for i in range(4)])

for p in itertools.product((0,1),repeat=int(n*(n-1)/2)):
  if degrees.sum() == sp.array(p).sum() * 2:  
    M = [ [ 0 for i in range(n) ] for i in range(n) ]
    
    q = 0
    for i in range(n):
      for j in range(n):
        if i < j:
          M[i][j], M[j][i] = p[q], p[q]
          q+=1
    
    sp_M = sp.array(M) 
    ds = sp.sum(sp_M,axis=0)
    
    if sp.all(ds == degrees) and sp.all( sp_M + sp_M.dot(sp_M) > 0 ):
      print(sp_M)
      G=nx.from_numpy_matrix(sp_M)
      nx.draw(G)
      plt.show()
      break
      
print("not found")

