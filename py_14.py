import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([6, 17, 34, 57, 86, 121])

def model_func(x, a, b, c):
    return a * x**2 + b * x + c

popt, pcov = curve_fit(model_func, x, y)
a, b, c = popt

print("--- FITTED POLYNOMIAL COEFFICIENTS ---")
print(f"Coefficient a (for x^2): {a:.4f}")
print(f"Coefficient b (for x):   {b:.4f}")
print(f"Coefficient c (constant): {c:.4f}")
print(f"\nFitted Equation: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}\n")

x_smooth = np.linspace(min(x), max(x), 200)
y_smooth = model_func(x_smooth, a, b, c)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Original Data Points', zorder=5)
plt.plot(x_smooth, y_smooth, color='blue', linestyle='-', label='Fitted 2nd-Degree Polynomial', linewidth=2)

plt.title('Polynomial Curve Fitting using SciPy')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
