#!/usr/bin/env python3

ds = [5,5,5,5]+[4 for _ in range(12)]

n = len(ds)

for r in range(1,n):
  if sum(ds[:r]) <= r*(r-1)+sum(map(lambda x: min(r,x),ds[r:])):
    pass
  else:
    print(r)
    print("FAIL")
    exit()
print("SUCCESS")