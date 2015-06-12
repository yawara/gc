import networkx as nx
from create_random import *

def base():
  G = nx.Graph()
  
  for i in range(4):
    for j1 in range(8):
      for k in range(3):
        G.add_edge((i,j1,"up",0),(i,j1,"mid",k))
        G.add_edge((i,j1,"up",1),(i,j1,"mid",k))
        G.add_edge((i,j1,"mid",k),(i,j1,"down",k))
        G.add_edge((i,j1,"down",0),(i,j1,"down",1))
        G.add_edge((i,j1,"down",1),(i,j1,"down",2))
        G.add_edge((i,j1,"down",2),(i,j1,"down",0))
      for j2 in range(8):
        if j1 < j2:
          G.add_edge((i,j1,"up",0),(i,j2,"up",1))
          G.add_edge((i,j1,"up",1),(i,j2,"up",0))
          for k in range(3):
            G.add_edge((i,j1,"mid",k),(i,j2,"down",(k+1)%3))
            G.add_edge((i,j1,"down",k),(i,j2,"mid",(k+2)%3))
            
  return G


def n256_d22():
  G = base()
  
  for i1 in range(4):
    for i2 in range(4):
      if i1 < i2:
        for j in range(8):
          G.add_edge((i1,j,"mid",0),(i2,j,"mid",1))
          G.add_edge((i1,j,"mid",0),(i2,j,"down",0))
          G.add_edge((i1,j,"mid",0),(i2,j,"up",1))
          
          G.add_edge((i1,j,"down",1),(i2,j,"mid",1))
          G.add_edge((i1,j,"down",1),(i2,j,"down",0))
          G.add_edge((i1,j,"down",1),(i2,j,"up",1))
          
          G.add_edge((i1,j,"mid",1),(i2,j,"mid",0))
          G.add_edge((i1,j,"mid",1),(i2,j,"mid",2))
          G.add_edge((i1,j,"mid",1),(i2,j,"down",0))
          
          G.add_edge((i1,j,"down",2),(i2,j,"mid",0))
          G.add_edge((i1,j,"down",2),(i2,j,"up",0))
          G.add_edge((i1,j,"down",2),(i2,j,"up",1))
          
          G.add_edge((i1,j,"mid",2),(i2,j,"down",1))
          G.add_edge((i1,j,"mid",2),(i2,j,"down",2))
          G.add_edge((i1,j,"mid",2),(i2,j,"up",0))
          
          G.add_edge((i1,j,"down",0),(i2,j,"down",1))
          G.add_edge((i1,j,"down",0),(i2,j,"down",2))
          G.add_edge((i1,j,"down",0),(i2,j,"up",0))
          
          G.add_edge((i1,j,"up",0),(i2,j,"mid",0))
          G.add_edge((i1,j,"up",0),(i2,j,"down",1))
          G.add_edge((i1,j,"up",0),(i2,j,"mid",2))
          
          G.add_edge((i1,j,"up",1),(i2,j,"mid",1))
          G.add_edge((i1,j,"up",1),(i2,j,"down",2))
          G.add_edge((i1,j,"up",1),(i2,j,"mid",2))
  
  for j in range(8):
    G.add_edge((0,j,"up",0),(1,j,"up",0))
    G.add_edge((0,j,"up",0),(1,j,"up",1))
    G.add_edge((0,j,"up",0),(3,j,"up",0))
    
    G.add_edge((0,j,"up",1),(2,j,"up",0))
    G.add_edge((0,j,"up",1),(2,j,"up",1))
    G.add_edge((0,j,"up",1),(3,j,"up",0))
    
    G.add_edge((1,j,"up",0),(2,j,"up",0))
    G.add_edge((1,j,"up",0),(3,j,"up",1))
    
    G.add_edge((1,j,"up",1),(2,j,"up",0))
    G.add_edge((1,j,"up",1),(3,j,"up",1))
    
    G.add_edge((2,j,"up",1),(3,j,"up",0))
    G.add_edge((2,j,"up",1),(3,j,"up",1))
    
    for k in range(3):
      G.add_edge((0,j,"mid",k),(1,j,"mid",k))
      G.add_edge((0,j,"mid",k),(1,j,"down",(k+1)%3))
      G.add_edge((0,j,"mid",k),(3,j,"mid",k))

      G.add_edge((0,j,"down",(k+1)%3),(2,j,"mid",k))
      G.add_edge((0,j,"down",(k+1)%3),(2,j,"down",(k+1)%3))
      G.add_edge((0,j,"down",(k+1)%3),(3,j,"mid",k))

      G.add_edge((1,j,"mid",k),(2,j,"mid",k))
      G.add_edge((1,j,"mid",k),(3,j,"down",(k+1)%3))

      G.add_edge((1,j,"down",(k+1)%3),(2,j,"mid",k))
      G.add_edge((1,j,"down",(k+1)%3),(3,j,"down",(k+1)%3))

      G.add_edge((2,j,"down",(k+1)%3),(3,j,"mid",k))
      G.add_edge((2,j,"down",(k+1)%3),(3,j,"down",(k+1)%3))
  
  return G
       
          
          
          