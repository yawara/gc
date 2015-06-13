#!/usr/bin/env python3

import networkx as nx
from create_random import *

def base():
  G = nx.Graph()
  
  for i in range(4):
    for j1 in range(8):
      for k in range(3):
        G.add_edge((i,j1,"up",0),(i,j1,"mid",k))
        G.add_edge((i,j1,"up",1),(i,j1,"mid",k))
        G.add_edge((i,j1,"mid",k),(i,j1,"down",k))
        G.add_edge((i,j1,"down",0),(i,j1,"down",1))
        G.add_edge((i,j1,"down",1),(i,j1,"down",2))
        G.add_edge((i,j1,"down",2),(i,j1,"down",0))
      for j2 in range(8):
        if j1 < j2:
          G.add_edge((i,j1,"up",0),(i,j2,"up",1))
          G.add_edge((i,j1,"up",1),(i,j2,"up",0))
          for k in range(3):
            G.add_edge((i,j1,"mid",k),(i,j2,"down",(k+1)%3))
            G.add_edge((i,j1,"down",k),(i,j2,"mid",(k+2)%3))
            
  return G

def n256_d13():
  G = base()
  
  for i1 in range(4):
    for i2 in range(4):
      if i1 < i2:
        for j in range(8):
          for k in range(2):
            G.add_edge((i1,j,"up",k),(i2,j,"up",k))
          for k in range(3):
            G.add_edge((i1,j,"mid",k),(i2,j,"mid",k))
            G.add_edge((i1,j,"down",k),(i2,j,"down",k))
  
  return G

def n256_d16():
  G = n256_d13()
  
  for i1 in range(4):
    for i2 in range(4):
      if i1 < i2:
        for j in range(8):
          for k in range(2):
            G.add_edge((i1,j,"up",k),(i2,(j+1)%8,"up",(k+1)%2))
          for k in range(3):
            G.add_edge((i1,j,"mid",k),(i2,(j+1)%8,"mid",(k+1)%3))
            G.add_edge((i1,j,"down",k),(i2,(j+1)%8,"down",(k+1)%3))
  
  return G
  
G = n256_d16()
print(len(G))
print(nx.diameter(G))
print(set(G.degree().values()))
print(max_avg_for_matrix(nx.shortest_path_length(G)))
