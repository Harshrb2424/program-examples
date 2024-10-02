from scipy import integrate

# Function to integrate
def integrand(x):
    return x**2

# Perform integration
result, error = integrate.quad(integrand, 0, 3)
print(f"Integral result from 0 to 3: {result:.2f}")