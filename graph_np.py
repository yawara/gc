#import networkx as nx
#from matplotlib import pyplot as plt
import numpy as np
import itertools

n=8
degrees = np.array([3 for i in range(8)])

for c in itertools.combinations(range(n*(n-1)//2),degrees.sum()//2):
    M = [ [ 0 for i in range(n) ] for i in range(n) ]
    
    p=[0 for i in range(n*(n-1)//2)]
    for i in c:
      p[i] = 1
      
    q = 0
    for i in range(n):
      for j in range(n):
        if i < j:
          M[i][j], M[j][i] = p[q], p[q]
          q+=1
    
    np_M = np.array(M) 
    ds = np.sum(np_M,axis=0)
    
    if degrees[0] == ds[0]:
      if np.all(ds == degrees) and np.all( np_M + np_M.dot(np_M) > 0):
        print(np_M)
        G=nx.from_numpy_matrix(np_M)
        #nx.draw(G)
        #plt.show()
        break

print("not found")

