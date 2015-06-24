#!/usr/bin/env python3
import pp
import pyprimes

def order(p,n,m):
  N = p**(n*m)
  M = p**(n*(m-1))
  return N**2 + N*M + M**2

def degree(p,n,m):
  N = p**(n*m)
  M = p**(n*(m-1))
  return N + M

def pair(p,n,m):
  return order(p,n,m),degree(p,n,m)

def search(max_p=1000,max_k=100,max_n=5,max_m=2):
  qs = []
  for p in pyprimes.primes_below(max_p+1):
    for k in range(1,max_k+1):
      qs.append(p**k)
  qs.sort()
  print("constructed qs", len(qs))
  
  i = 0
  for q in qs:
    print(i)
    for m in range(2,max_m+1):
      for n in range(1,max_n+1):
        print(n,m)
        tmp = pair(q,n,m)
        if pp.is_ddp_new(*tmp):
          print(tmp)
          print(p,k,n,m)
          print("")
    i+=1