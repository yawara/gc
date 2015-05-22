#!/usr/bin/env python3

primes = [ 2, 3, 5, 7, 11, 13, 17 ]

rtv = []

for p in primes:
  for k in range(1, 6):
    q = p ** k
    n = q ** 2 + q + 1
    rtv.append(n)
    
rtv.sort()
print(rtv)