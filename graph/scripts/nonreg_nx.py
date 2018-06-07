#!/usr/bin/env python3 
import networkx as nx
from matplotlib import pyplot as plt
import sys

n = int(sys.argv[1])
if n == 11:
  ds = [4 for _ in range(3)]+[3 for _ in range(8)] 
elif n == 5:
  ds = [2 for _ in range(5)]
elif n == 6:
  ds = [3 for _ in range(2)] + [2 for _ in range(4)]
elif n == 7:
  ds = [3 for _ in range(4)] + [2 for _ in range(3)]
elif n == 8:
  ds = [3 for _ in range(8)]
elif n == 9:
  ds = [4] + [3 for _ in range(8)]
elif n == 10:
  ds = [3 for _ in range(10)]
elif n == 11:
  ds = [4 for _ in range(3)] + [3 for _ in range(8)]
elif n == 12:
  ds = [4 for _ in range(10)] + [3 for _ in range(2)]
elif n == 13:
  ds = [4 for _ in range(9)] + [3 for _ in range(4)]

edges = sum(ds)/2
  

while 1:
  G=nx.gnm_random_graph(n,edges)
  if nx.is_connected(G):
    degrees = list(G.degree().values())
    degrees.sort(reverse=True)
    flag = True
    for i in range(len(ds)):
      if degrees[i] != ds[i]:
        flag = False
        break
    if flag:
      diameter = nx.diameter(G)
      if diameter == 2:
        print(G)
        nx.draw(G)
        plt.show()
        exit()
