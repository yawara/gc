#!/usr/bin/env python3
import networkx as nx
from matplotlib import pyplot as plt

def draw(G):
  nx.draw_networkx(G)
  plt.show()

def check(G):
  if len(G.nodes()) == 10:
    return nx.is_isomorphic(nx.petersen_graph(),G)
  elif nx.diameter(G) == 2:
    ds = list(nx.degree(G).values())
    if max(ds) == min(ds) or max(ds) == min(ds) + 1:
      return True
  return False

def not_used_label(G):
  for i in range(1000):
    if not i in G.nodes():
      return i

def not_used_label_pair(G):
  for i in range(1000):
    for j in range(i+1, 1000):
      if not i in G.nodes() and not j in G.nodes():
        return i, j

def not_used_five_labels(G):
  for i in range(1000):
    for j in range(1000):
      for k in range(1000):
        pass
      
# return the graph duplicated given one node
def dup_node(G, node):
  if node in G.nodes():
    H = G.copy()
    node_dup = not_used_label(G)
    for neighbor in nx.all_neighbors(G, node):
      H.add_edge(node_dup ,neighbor)
    return H
  else:
    raise Exception("no the node in G")

# return the graph duplicated give two nodes
# The node1 and node2 are NOT commutative!!!
def dup_node2(G, node1, node2):
  if node1 in nx.all_neighbors(G, node2):
    H = G.copy()
    node1_dup, node2_dup = not_used_label_pair(G)
    for neighbor_node1 in nx.all_neighbors(G, node1):
      if neighbor_node1 != node2:
        H.add_edge(node1_dup,neighbor_node1)
    for neighbor_node2 in nx.all_neighbors(G, node2):
      if neighbor_node2 != node1:
        H.add_edge(node2_dup,neighbor_node2)
    H.add_edge(node1_dup, node2_dup)
    H.add_edge(node2, node2_dup)
    return H
  else:
    raise Exception("the two nodes are not connected")

def odp8():
  G = odp(7)
  for node in G.nodes():
    if nx.degree(G, node) == 3:
      if [2,2,2] == list(map(lambda p: nx.degree(G,p) , nx.all_neighbors(G,node))):
        return dup_node(G,node)

def odp9():
  G = odp(7)
  for node in G.nodes():
    if nx.degree(G, node) == 3:
      if [2,2,2] == list(map(lambda p: nx.degree(G,p) , nx.all_neighbors(G,node))):
        return dup_node2(G, node, list(nx.all_neighbors(G,node))[0])

def dup_node5(G,nodes):
  nodes.append(nodes[0])
  iter_nodes = iter(nodes)
  for node1, node2 in zip(iter_nodes,iter_nodes):
    if not node2 in nx.all_neighbors(node1):
      raise Exception("the five nodes must be pentagon")
  
  H = G.copy()
  
  
# nodes are labed (i, j, k) 
def odp13():
  G = nx.empty_graph()
  for j in range(4):
    G.add_edge(0,(1,j))
    for k in range(2):
      G.add_edge((1,j),(2,j,k))
  for j in range(3):
    for k in range(2):
      G.add_edge((2,3,k),(2,j,k))
      G.add_edge((2,j,k),(2,(j+1)%3,(k+1)%2))
  return G

def odp14():
  G = odp13()
  for node in G.nodes():
    if nx.degree(G, node) == 4:
      if [3,3,3,3] == list(map(lambda p: nx.degree(G,p) , nx.all_neighbors(G,node))):
        return dup_node(G, node)
  
def odp(n):
  if n <= 1:
    raise Exception("The order of graph is greater than 1!!!")
  elif n <= 3:
    G = nx.path_graph(n)
  elif n <= 5:
    G = nx.cycle_graph(n)
  elif n == 6:
    G = dup_node(odp(5),0)
  elif n == 7:
    G = dup_node2(odp(5),0,1)
  elif n == 8:
    G = odp8()
  elif n == 9:
    G = odp9()
  elif n == 10:
    G = nx.petersen_graph()
  elif n == 11:
    G = dup_node(odp(10),0)
  elif n == 12:
    G = dup_node2(odp(10),0,1)
  elif n == 13:
    G = odp13()
  elif n == 14:
    G = odp14()
  #elif n % 5 == 0
  #  G = five_graph()
  #elif n == 16:
    
  return G

def order_diameter_problem(n , diameter=2):
  if diameter != 2:
    raise Exception("I DON'T KNOW!")
  if n <= 15:
    optimized = True
  elif n == 21 or n == 22:
    optimized = True
  G = odp(n)
  return G, optimized
