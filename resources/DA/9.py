import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Sample data for visualizations
x = np.linspace(0, 10, 30)
y = np.sin(x)
z = np.cos(x)
data = np.random.randint(1, 10, size=5)

# Bar Chart
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.bar(range(len(data)), data, color='blue')
plt.title('Bar Chart')

# Column Chart
plt.subplot(2, 3, 2)
plt.barh(range(len(data)), data, color='green')
plt.title('Column Chart')

# Line Chart
plt.subplot(2, 3, 3)
plt.plot(x, y, '-o', color='red')
plt.title('Line Chart')

# Scatter Plot
plt.subplot(2, 3, 4)
plt.scatter(x, y, color='purple')
plt.title('Scatter Plot')

# 3D Cubes Visualization
ax = plt.subplot(2, 3, 5, projection='3d')
for c, z_val in zip(['r', 'g', 'b', 'y', 'c'], [10, 20, 30, 40, 50]):
    xs = np.arange(20)
    ys = np.random.rand(20)
    ax.bar(xs, ys, zs=z_val, zdir='y', color=c, alpha=0.8)
plt.title('3D Cubes')

plt.tight_layout()
plt.show()
