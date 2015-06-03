#!/usr/bin/env python3
from scipy import sparse
import scipy as sp
import networkx as nx
import numpy as np
import sys

G=nx.read_adjlist(sys.argv[1])
M=nx.to_scipy_sparse_matrix(G)
D=M+M.dot(M)
result = sp.all(D.toarray()>0)
if result:
    print(result)
    print("OKKKKKKKKKK!!!!!!!")
