#import networkx as nx
#from matplotlib import pyplot as plt
import scipy as sp
import itertools
from multiprocessing import Pool

n=9
degrees = sp.array([4]+[3 for i in range(8)])
  
def f(c):
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

  sp_M = sp.array(M)

  ds = sp.sum(sp_M,axis=0)

  check_degree = True
  for i in range(n):
    if ds[i] != degrees[i]:
      check_degree = False
      break

  if check_degree:
    if sp.all( sp_M + sp_M.dot(sp_M) > 0 ):
      print(sp_M)
      #break

with Pool(processes=4) as pool:
  pool.map(f,itertools.combinations(range(n*(n-1)//2),degrees.sum()//2))
  #print("not found")

