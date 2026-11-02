import numpy as np

def q11_matrix_properties():
    print("--- Matrix Properties Program ---")
    n = int(input("Enter the dimension (N) for an NxN square matrix: "))
    
    print(f"\nEnter the elements for the {n}x{n} matrix row by row.")
    print("Separate elements in a row by spaces:")
    
    matrix = []
    for i in range(n):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != n:
                    print(f"Please enter exactly {n} numbers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")
                
    np_matrix = np.array(matrix)
    print("\nInput Matrix:\n", np_matrix)
    
    # 1. Compute Determinant
    determinant = np.linalg.det(np_matrix)
    print(f"\nDeterminant: {round(determinant, 4)}")
    
    # 2. Compute Rank
    rank = np.linalg.matrix_rank(np_matrix)
    print(f"Rank: {rank}")
    
    # 3. Compute Inverse (requires determinant != 0)
    # Using a small threshold (1e-10) to account for floating point inaccuracies
    if abs(determinant) > 1e-10:
        inverse = np.linalg.inv(np_matrix)
        print("\nInverse Matrix:\n", np.round(inverse, 4))
    else:
        print("\nInverse: The matrix is singular (determinant is 0), so it cannot be inverted.")

if __name__ == "__main__":
    q11_matrix_properties()
