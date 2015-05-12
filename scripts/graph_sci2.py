#import networkx as nx
#from matplotlib import pyplot as plt
import scipy as sp
import itertools

def check_diameter(M):
  return sp.all( M + M.dot(M) > 0 )

def check_degree(ds1,ds2):
  return sp.all( ds1 == ds2 )

n=8
degrees = sp.array([3 for i in range(8)])

for c in itertools.combinations(range(n*(n-1)//2),degrees.sum()//2):
    M = sp.zeros((n,n))
    
    p=[0 for i in range(n*(n-1)//2)]
    for i in c:
      p[i] = 1
      
    q = 0
    for i in range(n):
      for j in range(n):
        if i < j:
          M[i][j], M[j][i] = p[q], p[q]
          q+=1
    
    ds = sp.sum(M,axis=0)
    if check_diameter(M) and check_degree(ds, degrees):
        print(M)
        #G=nx.from_numpy_matrix(M)
        #nx.draw(G)
        #plt.show()
        break

print("not found")

