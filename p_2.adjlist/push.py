#!/usr/bin/env python3
from pp import *
import networkx as nx
import sys


if __name__ == "__main__":
    n=int(sys.argv[1])
    outfile=sys.argv[1]+"_2.adjlist"
    G=get(n*n)
    H=nx.convert_node_labels_to_integers(G)
    nx.write_adjlist(H,outfile)
