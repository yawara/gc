#!/usr/bin/env python3
from comb import comb

import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import random, sys


def draw(M):
  G=nx.from_numpy_matrix(M)
  nx.draw(G)
  plt.show()

def is_diameter2(M):
  return np.all( M + M.dot(M) > 0 )

def solve(r,M,c_max_d,c_min_d):
  if c_max_d > n_max_d or c_min_d > n_min_d:
    pass
  elif r == n-1:
    last_d = M[r].sum()
    if last_d == max_d and c_max_d + 1 == n_max_d and is_diameter2(M):
      print(M)
      draw(M)
      exit()
    elif last_d == max_d - 1 and c_max_d == n_max_d and is_diameter2(M):
      print(M)
      draw(M)
      exit()
  else:
    left_d = max_d - M[r].sum()
    if left_d >= 0 and left_d <= n-r-1:
      if left_d == 0:
        for j in range(1,n-r):
          M[r][r+j], M[r+j][r] = 0,0
        solve(r+1,M.copy(),c_max_d+1,c_min_d)
      else:
        bits = [ 0, 1 ]
        random.shuffle(bits)
        for bit in bits: 
          for c in comb(n-r-1, left_d - bit):
            j=1
            for b in c:
              M[r][r+j],M[r+j][r]=b,b
              j+=1
            if bit == 0:
              solve(r+1,M.copy(),c_max_d+1,c_min_d)
            elif bit == 1:
              solve(r+1,M.copy(),c_max_d,c_min_d+1)

if __name__=='__main__':
  n=int(sys.argv[1])
  max_d=int(sys.argv[2])
  n_max_d=int(sys.argv[3])
  n_min_d= n - n_max_d
  
  if max_d > n - 1:
    raise Exception
  
  M = np.zeros((n,n))
  
  for c in comb(n-1,max_d):
    for j, b in enumerate(c):
      M[0][j+1],M[j+1][0]=b,b
    solve(1,M.copy(),1,0)