# To print L and U matrix
import numpy as np
#add the library to import lu
from scipy.linalg import lu
#add the code to get the L and U matrix
matrix=eval(input())
A = np.array(matrix)
P, L, U = lu(A)
print(L)
print(U)


# To print X matrix (solution to the equations)
import numpy as np
from scipy.linalg import lu, lu_solve, lu_factor
#add the library to import lu_factor, lu_solve
A = np.array([[3, 2, 7], [2, 3, 1], [3, 4, 1]])
B = np.array([4, 5, 7])
#add the code to get the solution of the matrix
lu_piv = lu_factor(A)
X = lu_solve(lu_piv, B)
print(X)

