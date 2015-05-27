from sage.all import *
import networkx as nx
from itertools import product

def dot_product(v,w,R):
  if len(v) != len(w):
    raise Exception("v and w must be same length")
  rtv = R.zero()
  for i in range(len(v)):
    rtv += v[i] * w[i]
  return rtv

def get(R):
  G = nx.Graph()
  V = product(R, repeat=3)
  
  zero_vec = (R.zero(), R.zero(), R.zero())
  
  G.add_node(zero_vec)
  
  Rp = list(R)
  Rp.remove(0)
  
  for v in V:
    if all(not (r*v[0],r*v[1],r*v[2]) in G for r in Rp):
      v[0].set_immutable()
      v[1].set_immutable()
      v[2].set_immutable()
      G.add_node((v[0],v[1],v[2]))
  
  G.remove_node(zero_vec)
  
  for line1, line2 in product(G, repeat=2):
    if line1 != line2 and dot_product(line1,line2,R) == R.zero():
      G.add_edge(line1,line2)
      
  return G