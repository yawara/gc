#!/usr/bin/env python3
from scipy import sparse
import scipy as sp
import networkx as nx
import numpy as np
import sys

M=nx.to_scipy_sparse_matrix(nx.read_adjlist(sys.argv[1]))
result = sp.all((M+M.dot(M)).toarray() > 0)
if result:
    print(result)
    print("OKKKKKKKKKK!!!!!!!")
