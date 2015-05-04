#!/usr/bin/env python3 
import networkx as nx
from matplotlib import pyplot as plt
import sys

n=int(sys.argv[1])

try:
  d=int(sys.argv[2])
except IndexError:
  pd=int(n**(3/4))
  if pd % 2 == 0:
    d = pd + 2
  else:
    d = pd + 1

while 1:
  G=nx.random_regular_graph(d,n)
  if nx.is_connected(G):
    diameter = nx.diameter(G)
    if diameter == 3 or diameter == 2:
      print(G)
      #nx.draw(G)
      #plt.show()
      exit()