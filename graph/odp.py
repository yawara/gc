#!/usr/bin/env python3
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np


def draw(G):
  values = [nx.degree(G,node)+sum(map(lambda n: nx.degree(G,n),nx.all_neighbors(G,node))) for node in G.nodes()]
  nx.draw_circular(G,node_color=values,with_label=True)
  plt.show()

  
def check(G):
  if len(G.nodes()) == 10:
    return nx.is_isomorphic(nx.petersen_graph(),G)
  elif nx.diameter(G) == 2:
    ds = list(nx.degree(G).values())
    if max(ds) == min(ds) or max(ds) == min(ds) + 1:
      return True
  return False


def ave_deg(G):
  return np.average(list(nx.degree(G).values()))


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
  elif len(nodes) == 3:
    return nodes[0] in nx.all_neighbors(G,nodes[1]) and nodes[1] in nx.all_neighbors(G,nodes[2])
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

    
def dup_node3(G, *nodes):
  if check_dup_nodes(G, *nodes):
    H = G.copy()
    labels = not_used_labels(G,3)
    
    H.add_nodes_from(labels)

    H.add_edge(nodes[0],labels[2])
    H.add_edge(nodes[1],labels[1])
    H.add_edge(nodes[2],labels[0])
    
    H.add_edge(labels[0],labels[1])
    H.add_edge(labels[1],labels[2])
    
    for i, label in enumerate(labels):
      for neighbor in nx.all_neighbors(G, nodes[i]):
        if not neighbor in nodes:
          H.add_edge(label, neighbor)
    
    return H
  
  
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

'''
DEFINITION: odp13()
                        (2,0,k) for k in range(2)
                                    |
                                  (1,0)
                                    |
(2,1,k) for k in range(2) - (1,1) - 0 - (1,3) - (2,3,k) for k in range(2)
                                    |
                                  (1,2)
                                    |
                        (2,2,k) for k in range(2)
'''
def to_str(*p):
  rtv = str(p[0])
  for i in p[1:]:
    rtv += "_"+str(i)
  return rtv

def odp13():
  G = nx.Graph()
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

      
def merge_nodes(G, *nodes):
  H = G.copy()
  H.remove_nodes_from(nodes)
  label = not_used_labels(G, 1)[0]
  H.add_node(label)
  for node in nodes:
    for neighbor in nx.all_neighbors(G, node):
      if not neighbor in nodes:
        H.add_edge(label, neighbor)
  return H


def mult5(q):
  if q == 1:
    return odp(5)
  else:
    return dup_node5(mult5(q-1),0,1,2,3,4)

  
def odp_mod5(n):
  q = n // 5
  r = n % 5
  if r == 0:
    print("0 mod 5")
    return mult5(q)
  elif r == 1:
    print("1 mod 5")
    return dup_node(mult5(q),0)
  elif r == 2:
    print("2 mod 5")
    return dup_node2(mult5(q),0,1)
  elif r == 3:
    print("3 mod 5")
    return dup_node3(mult5(q),0,1,2)
  elif r == 4:
    print("4 mod 5")
    return merge_nodes(mult5(q+1),0,5)

  
def odp22():
  G = nx.Graph()
  for j in range(5):
    G.add_edge(0,to_str(1,j))
    for k in range(3):
      G.add_edge(to_str(1,j),to_str(2,j,k))
  for j in range(4):
    for k in range(3):
      G.add_edge(to_str(2,4,k),to_str(2,j,k))
      G.add_edge(to_str(2,j,k),to_str(2,(j+1)%4,(k+1)%3))
  for j in range(2):
    for k in range(3):
      G.add_edge(to_str(2,j,k),to_str(2,j+2,k))
  return dup_node(G,0)


def mult8(q):
  if q < 3:
    raise Exception("Oops! q >= 3")
  
  G = nx.Graph()
  
  for i in range(q):
    for k in range(2):
      for l in range(3):
        G.add_edge((i,0,k),(i,1,l))
    for k in range(3):
      G.add_edge((i,1,k),(i,2,k))
    G.add_edge((i,2,0),(i,2,1))
    G.add_edge((i,2,1),(i,2,2))
    G.add_edge((i,2,2),(i,2,0))
  
  for i in range(q-1):
    for k in range(2):
      G.add_edge((q-1,0,k),(i,0,k))
    for k in range(3):
      G.add_edge((q-1,1,k),(i,2,k))
      G.add_edge((q-1,2,k),(i,1,(k+1)%3))
  
  for i in range(q-1):
    for j in range(q-1):
      if i < j:
        G.add_edge((i,0,0),(j,0,1))
        G.add_edge((i,0,1),(j,0,0))
        for k in range(3):
          G.add_edge((i,1,k),(j,2,(k+1)%3))
          G.add_edge((i,2,k),(j,1,(k-1)%3))
  
  return G  


def odp_mod8(n):
  q = n // 8
  r = n % 8
  
  if r > 3:
    raise Exception("mod8 accept r <= 2")
  
  G = mult8(q)
  
  if r == 0:
    print("0 mod 8")
    return G
  if r == 1:
    print("1 mod 8")
    return dup_node(G, (0,0,0))
  if r == 2:
    print("2 mod 8")
    return dup_node2(G, (0,0,0), (0,1,0))
  if r == 3:
    print("3 mod 8")
    return dup_node3(G, (0,0,0), (0,1,0), (0,2,0))

  
def mult7(q):
  if q < 3:
    raise Exception("Oops! q >= 3")
  
  G = nx.Graph()
  
  for i in range(q):
    for k in range(3):
      G.add_edge((i,0),(i,1,k))
      G.add_edge((i,1,k),(i,2,k))
    G.add_edge((i,2,0),(i,2,1))
    G.add_edge((i,2,1),(i,2,2))
    G.add_edge((i,2,2),(i,2,0))
  
  for i in range(q):
    for j in range(q):
      if i < j:
        G.add_edge((i,0),(j,0))
  
  for i in range(q-1):
    for k in range(3):
      G.add_edge((q-1,1,k),(i,2,k))
      G.add_edge((q-1,2,k),(i,1,(k+1)%3))
  
  for i in range(q-1):
    for j in range(q-1):
      if i < j:
        for k in range(3):
          G.add_edge((i,1,k),(j,2,(k+1)%3))
          G.add_edge((i,2,k),(j,1,(k-1)%3))
  
  return G


def mult6(q):
  if q < 3:
    raise Exception("Oops! q >= 3")
  
  G = nx.Graph()
  
  for i in range(q):
    for k in range(2):
      for l in range(2):
        G.add_edge((i,0,k),(i,1,l))
      G.add_edge((i,1,k),(i,2,k))
    G.add_edge((i,2,0),(i,2,1))
  
  for i in range(q-1):
    for k in range(2):
      G.add_edge((q-1,0,k),(i,0,k))
      G.add_edge((q-1,1,k),(i,2,k))
      G.add_edge((q-1,2,k),(i,1,(k+1)%2))
  
  for i in range(q-1):
    for j in range(q-1):
      if i < j:
        G.add_edge((i,0,0),(j,0,1))
        G.add_edge((i,0,1),(j,0,0))
        for k in range(2):
          G.add_edge((i,1,k),(j,2,(k+1)%2))
          G.add_edge((i,2,k),(j,1,(k+1)%2))

  return G  


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
  elif n == 22:
    G = odp22()
  elif n % 8 <= 3 and n // 8 > 2:
    G = odp_mod8(n)
  elif n % 7 == 0 and n // 7 > 2:
    print("0 mod 7")
    G = mult7(n//7)
  elif n % 7 == 3 and n // 7 > 2:
    print("3 mod 7")
    G = dup_node3(mult7(n//7),(0,2,0),(0,2,1),(0,2,2))
  elif n % 6 == 0 and n // 6 > 2:
    print("0 mod 6")
    G = mult6(n//6)
  elif n % 6 == 1 and n // 6 > 2:
    print("1 mod 6")
    G = dup_node(mult6(n//6),(0,1,0))
  else:
    G = odp_mod5(n) 
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
