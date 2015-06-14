from sage.all import *
from sage_poly import *

R = Zmod(4)
x = var('x')
P = PolynomialRing(R, x)

for p in P.polynomials(2):
  if R.is_field() and p in P.irreducible_element(2):
    pass
  else:
    if p in P.monics(2):
      Q = P.quotient(p)
      G = get(Q)
      show(G)
      print("")