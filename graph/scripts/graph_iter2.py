#!/usr/bin/env python3
from comb import comb

import networkx as nx
from matplotlib import pyplot as plt
import scipy as sp
import random, sys


n=int(sys.argv[1])
max_d=int(sys.argv[2])

#edges=w_edges/2

M = [ [ 0 for i in range(n) ] for i in range(n) ]

def is_diameter2(M):
  sp_M = sp.array(M)
  return sp.all( sp_M + sp_M.dot(sp_M) > 0 )

def clear(r):
  for j in range(n):
    M[r][j] == 0
    
def clear_sub(r):
  for j in range(r+1,n):
    M[r][j] == 0
  
def solve_row(r):
  if r == n - 1:
    last_d = sum(M[r])
    if (last_d == max_d or last_d == max_d - 1) and is_diameter2(M):
      sp_M = sp.array(M)
      print(sp_M)
      G=nx.from_numpy_matrix(sp_M)
      nx.draw(G)
      plt.show()
      exit()
    clear(r)
  else:
    left_d = max_d
    for i in range(r):
      M[r][i] = M[i][r]
      left_d-=1
    if left_d >=0:
      for c in comb(n-r-1,left_d):
        j = r+1
        for b in c:
          M[r][j] = b
          j+=1
        solve_row(r+1)
        clear_sub(r)
      for c in comb(n-r-1,left_d-1):
        j = r+1
        for b in c:
          M[r][j] = b
          j+=1
        solve_row(r+1)
        clear_sub(r)
    else:
      clear(r)
        
if __name__=='__main__':
  for i in range(max_d):
    M[0][i+1]
  solve_row(1)