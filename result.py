#!/usr/bin/env python3
from odp import *
import networkx as nx
import numpy as np

for n in range(5,100):
  G = odp(n)
  ave_deg = np.average(list(nx.degree(G).values()))
  print("n:",n)
  print("ave_deg:",ave_deg)
  print("")
  