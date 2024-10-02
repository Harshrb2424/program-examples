import numpy as np
import matplotlib.pyplot as plt

# Function to estimate coefficients
def estimate_coeff(x, y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x
    
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    
    return (b_0, b_1)

# Function to plot regression line
def plot_regression_line(x, y, b):
    plt.scatter(x, y, color = "m", marker = "o", s = 30)
    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color = "g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Main function to run the program
def main():
    # Data points
    x = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    y = np.array([11, 13, 12, 15, 17, 18, 18, 19, 20, 22])

    # Estimate coefficients
    b = estimate_coeff(x, y)
    print(f"Estimated coefficients:\nb_0 = {b[0]}, b_1 = {b[1]}")

    # Plot regression line
    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()