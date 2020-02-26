# Author: Luciano de Oliveira Daniel
# https://sites.google.com/site/professorlucianodaniel

import pprint
import scipy.linalg
from numpy import random
from scipy.io import savemat
import time

def pause():
    input("Press the <ENTER> key to continue...")


dim = int(input('Dimension of the square random matrix:'))
A = random.rand(dim, dim)
print('A:')
pprint.pprint(A)
savemat('calc_lu_01.mat', {'A_P': A})
#A = scipy.array([[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]])
t = time.time()
P, L, U = scipy.linalg.lu(A)
elapsed = time.time() - t
print('P:', '\n')
pprint.pprint(P)
savemat('calc_lu_02.mat', {'P_P': P})
print('L:', '\n')
pprint.pprint(L)
savemat('calc_lu_03.mat', {'L_P': L})
print('U:', '\n')
pprint.pprint(U)
savemat('calc_lu_04.mat', {'U_P': U})
print('LU elapsed time in PYTHON (executable) is:', elapsed, 'seconds', '\n')
print('"I have a paper afloat which I hold to be great guns" (Maxwell, J.C.)', '\n')
pause()