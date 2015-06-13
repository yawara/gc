#!/usr/bin/env python3
import networkx as nx
from create_random import *

"""
頂点を0〜65とする
i=0〜5とするときmod66で
(11i+1,11i+1+10)
(22i+6,22i+6+11)
(11i+2,11i+21)
(11i+3,11i+31)
(11i+4,11i+41)
(11i+5,11i+51)
を接続したあと
j=0-65で
(j,j+1)をつないで
最後に
頂点4と41を消去して3と5、40と42をつなぐと結構いい感じのグラフになるかも。暇あったらやってみて。

うまくいってたら256-3、4096-3、10000-3と64-4、256-4、4096-4くらいまでは一般化出来るかも
"""

def n66():
  G = nx.Graph()
  
  for i in range(6): # iは0~5まで動く。
    G.add_edge((11*i+1)%66,(11*i+1+10)%66)
    G.add_edge((22*i+6)%66,(22*i+6+11)%66)
    G.add_edge((11*i+2)%66,(11*i+21)%66)
    G.add_edge((11*i+3)%66,(11*i+31)%66)
    G.add_edge((11*i+4)%66,(11*i+41)%66)
    G.add_edge((11*i+5)%66,(11*i+51)%66)
    
  for j in range(65): # jは0~64まで動く。
    G.add_edge(j,j+1)
  G.add_edge(65,0) # 65だけ別処理で追加する。
  
  return G

def n64_d3():
  G = n66()
  
  G.remove_nodes_from([4,41])
  G.add_edges_from([(3,5),(40,42)])
  
  return G

def show(G):
  print("nodes:",len(G))
  print("diameter:",nx.diameter(G))
  print("degrees:",set(G.degree().values()))
  print("score:",max_avg_for_matrix(nx.shortest_path_length(G)))

"""
nodes: 64
diameter: 7
degrees: {3}
score: (7, 4.0188492063492065)
"""