import matplotlib.pyplot as plt

# Fixed: Both lists now have exactly 6 items
x = [1, 2, 3, 4, 5, 6]
y = [12, 26, 7, 22, 15, 20]  # Added '20' to match x length

# Create the bar chart with a label for the legend
plt.bar(x, y, color='skyblue', label='Value Distribution')
plt.plot(x, y, color='red', label='Data Points')  # Added scatter plot for data points

# Add titles and labels
plt.title('Bar Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the legend and show the plot
plt.legend()
plt.show()
