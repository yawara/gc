#import networkx as nx
#from matplotlib import pyplot as plt
import scipy as sp
from multiprocessing import Pool

n=9
degrees = sp.array([4]+[3 for i in range(10)])
log=2

def check(p):
  M = [ [ 0 for i in range(n) ] for i in range(n) ]
  q = 1
  for i in range(n):
    for j in range(n):
      if i < j:
        M[i][j], M[j][i] = p[-q], p[-q]
        q+=1

  sp_M = sp.array(M) 
  ds = sp.sum(sp_M,axis=0)

  if sp.all(ds == degrees) and sp.all( sp_M + sp_M.dot(sp_M) > 0 ):
    print(sp_M)
    #G=nx.from_numpy_matrix(sp_M)
    #nx.draw(G)
    #plt.show()
    #exit()

def comb(n,m,*p):
  if n==0 and m==0:
    check(p)
  elif m==0:
    comb(n-1,0,0,*p)
  elif n==m:
    comb(n-1,m-1,1,*p)
  else:
    comb(n-1,m,0,*p)
    comb(n-1,m-1,1,*p)

def c_bits_l(n):
  rts=[]
  def c_bits_l_aux(m,c,*p):
    if m==0:
      rts.append((c,list(p)))
    else:
      c_bits_l_aux(m-1,c+1,1,*p)
      c_bits_l_aux(m-1,c,0,*p)
  c_bits_l_aux(n,0)
  return rts

init = [0 for i in range(n-1-degrees[0])] + [1 for i in range(degrees[0])]
def f(c_bits):
  c=c_bits[0]
  bits=c_bits[1]
  comb((n-1)*(n-2)/2-log,degrees.sum()/2-degrees[0]-c,*(bits+init))

if __name__=='__main__':
  with Pool(processes=2**log) as pool:
    pool.map(f,c_bits_l(log))