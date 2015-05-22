#!/usr/bin/env python3
import networkx as nx
import numpy as np
from erdos import rtv

def get(p):
  lines = set()
  for i in range(p):
    for j in range(p):
      for k in range(p):
        if all(not ((a*i)%p,(a*j)%p,(a*k)%p) in lines for a in range(1,p)):
          lines.add((i,j,k)) 
  
  lines.remove((0,0,0))
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
  if max_d - min_d == 1 or max_d - min_d == 0:
    deg_ave = np.average(deg_vals)
    print("degree is safe:", deg_ave)
  
  print("diameter:", nx.diameter(G))
  print("node:", len(G.nodes()))
  if len(G.nodes()) in rtv:
    print("order in erdos nums")
  print("erodos bound:", deg_ave**2-deg_ave+1)