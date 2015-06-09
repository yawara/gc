import pyviennacl as p
import numpy as np
import sys 
n=int(sys.argv[1])

x = np.random.rand(n).astype(np.float32)
A = np.random.rand(n,n).astype(np.float32)


#x = np.array([1.0,2.0,3.0],dtype=np.float32)
#y = np.array([2.0,3.0,4.0],dtype=np.float32)
#A = np.array([[1,2,3],
#              [2,3,4],
#              [3,4,5]],dtype=np.float32)

v=p.Vector(x)
M=p.Matrix(A)
             
print(M**k)
print(A**k)
