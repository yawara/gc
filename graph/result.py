#!/usr/bin/env python3
from odp import *
import networkx as nx
import numpy as np

for n in range(5,101):
  G = odp(n)
  ave_deg = np.average(list(nx.degree(G).values()))
  print("n:",n)
  if not check(G):
    print("WHAT THE FACK")
  print("ave_deg:",ave_deg)
  print("")
  
