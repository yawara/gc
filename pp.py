#!/usr/bin/env python3
import networkx as nx
from matplotlib import pyplot as plt
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
  print("diameter:", nx.diameter(G))
  print("node:", len(G.nodes()))
  if len(G.nodes()) in rtv:
    print("FAIL")
  print(G.degree().values())