#!/usr/bin/env python3

import networkx as nx
from matplotlib import pyplot as plt
import scipy as sp
import random, sys

n=int(sys.argv[1])
max_d=int(sys.argv[2])

if len(sys.argv)==4:
  w_edges=int(sys.argv[3])
else:
  if n==5:
    w_edges = sp.array([2 for i in range(5)]).sum()
  elif n==6:
    w_edges = sp.array([3 for i in range(2)]+[2 for i in range(4)]).sum()
  elif n==7:
    w_edges = sp.array([3 for i in range(4)]+[2 for i in range(3)]).sum()
  elif n==8:
    w_edges = sp.array([3 for i in range(8)]).sum()
  elif n==9:
    w_edges = sp.array([4]+[3 for i in range(8)]).sum()
  elif n==10:
    w_edges = sp.array([3 for i in range(10)]).sum()
  elif n==11:
    w_edges = sp.array([4 for i in range(3)]+[3 for i in range(8)]).sum()

def check(p):
  M = [ [ 0 for i in range(n) ] for i in range(n) ]

  q=1
  for i in range(n):
    for j in range(n):
      if i < j:
        M[i][j], M[j][i] = p[-q], p[-q]
        q+=1

  sp_M = sp.array(M) 
  degrees = sp.sum(sp_M,axis=0)
  width_d = sp.amax(degrees) - sp.amin(degrees)
  
  if ( width_d == 0 or width_d == 1 ) and sp.all( sp_M + sp_M.dot(sp_M) > 0 ):
    print(sp_M)
    G=nx.from_numpy_matrix(sp_M)
    nx.draw(G)
    plt.show()
    exit()

def comb(n,m,*p):
  if n==0 and m==0:
    check(p)
  elif m==0:
    comb(n-1,0,0,*p)
  elif n==m:
    comb(n-1,m-1,1,*p)
  else:
    if random.choice([True,False]):
      comb(n-1,m-1,1,*p)
      comb(n-1,m,0,*p)
    else:
      comb(n-1,m,0,*p)
      comb(n-1,m-1,1,*p)

if __name__=='__main__':
  init = [0 for i in range(n-1-max_d)] + [1 for i in range(max_d)]
  comb((n-1)*(n-2)/2,w_edges/2-max_d,*init)
