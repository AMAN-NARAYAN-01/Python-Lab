import numpy as np
def matrix_operations():
    A = [[1, 2], 
         [3, 4]]  
    B = [[5, 6], 
         [7, 8]]
    print("Matrix A:", A)
    print("Matrix B:", B)
    #without Nupy
    print("\n--- Operations Without NumPy ---")
    
    addition = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    print("Addition:", addition)

    subtraction = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    print("Subtraction:", subtraction)

    multiplication = [[sum(A[i][k] * B[k][j] for k in range(len(B[0]))) for j in range(len(B))] for i in range(len(A))]
    print("Multiplication:", multiplication)

    transpose_A = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    print("Transpose of A:", transpose_A)
    #with numpy
    print("\n--- Operations With NumPy ---")
    np_A = np.array(A)
    np_B = np.array(B)    
    print("Addition:\n", np.add(np_A, np_B))
    print("Subtraction:\n", np.subtract(np_A, np_B))
    print("Multiplication:\n", np.dot(np_A, np_B))
    print("Transpose of A:\n", np.transpose(np_A))
matrix_operations()
