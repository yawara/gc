#!/usr/bin/env python3
import scipy as sp
import networkx as nx
from matplotlib import pyplot as plt

n=7
ds=[3 for i in range(4)]+[2 for i in range(3)]

def dammy_check(p):
  print(p)

def check(p):
  M=[[0 for i in range(n)] for i in range(n)]
  q = 1
  for i in range(n):
    for j in range(n):
      if i < j:
        M[i][j] = p[-q]
        q+=1
      elif i > j:
        if M[j][i] == p[-q]:
          M[i][j] = p[-q]
          q+=1
        else:
          raise Exception
  sp_M=sp.array(M)
  print(sp_M)
  if sp.all( sp_M + sp_M.dot( sp_M ) > 0):
    G=nx.from_numpy_matrix(sp_M)
    nx.draw(G)
    plt.show()

def comb(p_ds,m,k,*p):
    if m==0 and k==0:
      if p_ds==len(ds)-1:
        try:
          #print(str(len(p))+": ",end="")
          #dammy_check(p)
          check(p)
        except Exception:
          pass
          #print("not sutable")
      else:
        comb(p_ds+1,n-1,ds[p_ds+1],*p)
    elif k==0:
      comb(p_ds,m-1,k,0,*p)
    elif m==k:
      comb(p_ds,m-1,k-1,1,*p)
    else:
      comb(p_ds,m-1,k-1,1,*p)
      comb(p_ds,m-1,k,0,*p)
         
if __name__=="__main__":
  comb(0,n-1,ds[0])