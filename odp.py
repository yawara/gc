#!/usr/bin/env python3
import networkx as nx
from matplotlib import pyplot as plt

def draw(G):
  values = [nx.degree(G,node)+sum(map(lambda n: nx.degree(G,n),nx.all_neighbors(G,node))) for node in G.nodes()]
  nx.draw_networkx(G,node_color=values,with_label=True)
  plt.show()

def check(G):
  if len(G.nodes()) == 10:
    return nx.is_isomorphic(nx.petersen_graph(),G)
  elif nx.diameter(G) == 2:
    ds = list(nx.degree(G).values())
    if max(ds) == min(ds) or max(ds) == min(ds) + 1:
      return True
  return False

def not_used_labels(G, n):
  max_value = 0
  for node in G.nodes():
    if type(node) == int and node > max_value:
      max_value = node
  return list(range(max_value+1,max_value+n+1))

def check_dup_nodes(G, *nodes):
  for node in nodes:
    if not node in G.nodes():
      return False
  if len(nodes) == 1:
    return True
  elif len(nodes) == 2:
    return nodes[0] in nx.all_neighbors(G,nodes[1])
  elif len(nodes) == 5:
    nodes_f = iter(list(nodes)+[nodes[0]])
    for a, b in zip(nodes_f,nodes_f):
      if not a in nx.all_neighbors(G,b):
        return False
    return True
  else:
    return False

# return the graph duplicated given one node
def dup_node(G, node):
  if check_dup_nodes(G, node):
    H = G.copy()
    node_dup = not_used_labels(G,1)[0]
    for neighbor in nx.all_neighbors(G, node):
      H.add_edge(node_dup ,neighbor)
    return H
  else:
    raise Exception("no the node in G")

# return the graph duplicated give two nodes
# The node1 and node2 are NOT commutative!!!
def dup_node2(G, node1, node2):
  if check_dup_nodes(G, node1, node2):
    H = G.copy()
    labels = not_used_labels(G,2)
    node1_dup, node2_dup = labels[0], labels[1]
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

def dup_node5(G,*nodes):
  if check_dup_nodes(G,*nodes):
    H = G.copy()
    labels = not_used_labels(G,5)
    
    H.add_nodes_from(labels)
    
    H.add_edge(nodes[0],labels[0])
    H.add_edge(nodes[1],labels[2])
    H.add_edge(nodes[2],labels[4])
    H.add_edge(nodes[3],labels[1])
    H.add_edge(nodes[4],labels[3])
    
    H.add_edge(labels[0],labels[1])
    H.add_edge(labels[1],labels[2])
    H.add_edge(labels[2],labels[3])
    H.add_edge(labels[3],labels[4])
    H.add_edge(labels[4],labels[0])
    
    for i, label in enumerate(labels):
      for neighbor in nx.all_neighbors(G, nodes[i]):
        if not neighbor in nodes:
          H.add_edge(label, neighbor)
    
    return H
  else:
    raise Exception("the five nodes are not a pentagon!!!")

def to_str(*p):
  rtv = str(p[0])
  for i in p[1:]:
    rtv += "_"+str(i)
  return rtv
  
# nodes are labed (i, j, k) 
def odp13():
  G = nx.empty_graph()
  for j in range(4):
    G.add_edge(0,to_str(1,j))
    for k in range(2):
      G.add_edge(to_str(1,j),to_str(2,j,k))
  for j in range(3):
    for k in range(2):
      G.add_edge(to_str(2,3,k),to_str(2,j,k))
      G.add_edge(to_str(2,j,k),to_str(2,(j+1)%3,(k+1)%2))
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
    G = dup_node5(odp(5),0,1,2,3,4)
    #G = nx.petersen_graph()
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
