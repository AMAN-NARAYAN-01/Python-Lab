import numpy as np
from scipy.integrate import quad
from scipy.misc import derivative
def f(x):
    return x**3 * np.sin(x)
x_val = 2.0
h_val = 1e-5 

first_deriv = derivative(f, x_val, dx=h_val, n=1, order=3)
second_deriv = derivative(f, x_val, dx=h_val, n=2, order=5)

print("--- NUMERICAL DIFFERENTIATION ---")
print(f"Function: f(x) = x^3 * sin(x)")
print(f"At x = {x_val}:")
print(f"  First Derivative  (f'): {first_deriv:.6f}")
print(f"  Second Derivative (f''): {second_deriv:.6f}\n")

a, b = 0.0, np.pi

integral_val, abs_error = quad(f, a, b)

print("--- NUMERICAL INTEGRATION ---")
print(f"Definite Integral of f(x) from {a} to {b} (approx 3.1416):")
print(f"  Calculated Value: {integral_val:.6f}")
print(f"  Estimated Error:  {abs_error:.2e}")
