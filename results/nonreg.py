#!/usr/bin/env python3 
import networkx as nx
from matplotlib import pyplot as plt
import sys
from findgds_nx import random_graph

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
#try:
#  d=int(sys.argv[2])
#except IndexError:
#  pd=int(n**(3/4))
#  if pd % 2 == 0:
#    d = pd + 2
#  else:
#    d = pd + 1

while 1:
  G=random_graph(ds,n)
  if nx.is_connected(G):
    diameter = nx.diameter(G)
    if diameter == 2:
      print(G)
      nx.draw(G)
      plt.show()
      exit()
