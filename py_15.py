import numpy as np
from scipy.optimize import minimize

def objective_function(vars):
    x = vars[0]
    y = vars[1]
    return (x - 2)**2 + (y - 2)**2

def run_optimization():
    initial_guess = np.array([0.0, 0.0])    
    result = minimize(objective_function, initial_guess, method='BFGS')
    print("--- SciPy Optimization Results ---")
    if result.success:
        print("Status: Optimization successful!")
        print(f"Optimal coordinates: x = {result.x[0]:.4f}, y = {result.x[1]:.4f}")
        print(f"Minimum function value: {result.fun:.4f}")
        print(f"Iterations required: {result.nit}")
    else:
        print("Status: Optimization failed.")
        print(f"Reason: {result.message}")

if __name__ == "__main__":
    run_optimization()
