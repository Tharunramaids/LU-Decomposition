# LU Decomposition 

## AIM:
To write a program to find the LU Decomposition of a matrix.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Moodle-Code Runner

## Algorithm
 ### Step 1:
 Import the numpy module to use the build in functions for calculation

### Step 2:
Prepare the lists form each linear equations and assign is np.array()

### Step 3:
Using the np.linalg.solve(),we can find the solution 

### Step 4:
End of the program 

## Program:
(i) To find the L and U matrix
```
/*
Program to find the L and U matrix.
Developed by: Tharun R
RegisterNumber: 24005919
*/
import numpy as np
from scipy.linalg import lu
matrix=eval(input())
A = np.array(matrix)
P, L, U = lu(A)
print(L)
print(U)
```
(ii) To find the LU Decomposition of a matrix
```
/*
Program to find the LU Decomposition of a matrix.
Developed by: Tharun R
RegisterNumber: 24005919
*/
import numpy as np
from scipy.linalg import lu, lu_solve, lu_factor
A = np.array([[3, 2, 7], [2, 3, 1], [3, 4, 1]])
B = np.array([4, 5, 7])
lu_piv = lu_factor(A)
X = lu_solve(lu_piv, B)
print(X)

```

## Output:
![alt text](image.png)
![alt text](image-1.png)


## Result:
Thus the program to find the LU Decomposition of a matrix is written and verified using python programming.

