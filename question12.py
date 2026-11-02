import numpy as np

def q12_eigen_properties():
    n = int(input("Enter the dimension (n) for an nxn square matrix: "))
    print(f"Enter the elements for the {n}x{n} matrix row by row (space-separated):")
    
    matrix = []
    for _ in range(n):
        matrix.append(list(map(float, input().split())))
        
    np_matrix = np.array(matrix)
    
    eigenvalues, eigenvectors = np.linalg.eig(np_matrix)
    
    print("\nEigenvalues:\n", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)

if __name__ == "__main__":
    q12_eigen_properties()


