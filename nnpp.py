#!/usr/bin/env python3
import networkx as nx
import numpy as np
from erdos import rtv

def gcd(a,b):
  if a > b:
    a, b = b, a
  while a > 0:
    a, b = b%a, a
  return b
  
def get(p):
  lines = set()
  for i in range(p):
    for j in range(p):
      for k in range(p):
        if (i, j, k) == (0, 0, 0):
          pass
        else:
          flag = True
          for a in range(1,p):
            if gcd(a,p) == 1:
              if ((a*i)%p,(a*j)%p,(a*k)%p) in lines:
                flag = False
                break
          if flag:
            lines.add((i,j,k))
            
  lines.add((0,0,0))
  #print(lines)

  G = nx.Graph()

  for line1 in lines:
    for line2 in lines:
      if line1 != line2:
        norm = 0
        for i in range(3):
          norm += line1[i]*line2[i]
        if norm % p == 0:
          G.add_edge(line1,line2)

  return G

def show(p):
  G = get(p)
  deg_vals = list(G.degree().values())
  max_d = max(deg_vals)
  min_d = min(deg_vals)
  deg_ave = np.average(deg_vals)
  if max_d - min_d == 1 or max_d - min_d == 0:
    print("degree is safe:", deg_ave)
  else:
    print("DEGFAIL",deg_ave)
  print("diameter:", nx.diameter(G))
  print("node:", len(G.nodes()))
  if len(G.nodes()) in rtv:
    print("order in erdos nums")
  erdos_bound = deg_ave**2-deg_ave+1
  print("erodos bound:", erdos_bound)
  print(int(100*len(G.nodes())/erdos_bound),"%")
  