import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4]
y = [10, 15, 7, 20]

# Create a line plot
plt.plot(x, y, marker='o', label='Sales')

plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Monthly Sales')
plt.legend()

# Show the plot
plt.show()