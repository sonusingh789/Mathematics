#%%
import numpy as np

A = np.array(
    [
        [1,2],
        [3,4],
    ]
)
B = np.array(
    [
        [1,2],
        [3,4],
    ]
)

print("Addition \n",A+B)
print("Subtraction \n",A-B)

C = 2*A
print(" Scalar Multiplication \n",C)


result = np.dot(A,B)
print(" Matrix Multiplication \n",result)

I = np.eye(3)
print(" Identity Matrix I\n",I)

Z = np.zeros((2,3))
print(" Zero Matrix \n",Z)

D = np.diag([1,2,3])
print(" Diagonal Matrix \n",D)

# Determinants and Inverse of a Matrix


det = np.linalg.det(A)
print(" Determinant of A \n",det)


inverse = np.linalg.inv(A)
print(" Inverse of A \n",inverse)

eigenValues = np.linalg.eig(A)
print(" Eigenvalues of A \n",eigenValues)

# Matrix Decomposition

# computing SVD in Numpy

U,S,Vt = np.linalg.svd(A)
print("  U \n",U)
print(" Singular value S \n",S)
print(" V Transpose U \n",Vt)

Sigma = np.zeros((3,3))
np.fill_diagonal(Sigma,S)
reconstructed = U @ Sigma @ Vt
# or np.dot(np.dot(U, Sigma), Vt) same @ is used for multiplication
print("Reconstruction of A \n",reconstructed)
