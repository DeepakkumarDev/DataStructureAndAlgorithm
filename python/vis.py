import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Create a DataFrame with your data
data = {
    'Product ID': [1, 2, 3, 4, 5],
    'Sales Volume': [10, 12, 38, 30, 32],
    'Customer Satisfaction': [12, 4, 20, 15, 50]
}

df = pd.DataFrame(data)

# Prepare data for smooth curves
x = df['Product ID']
y_sales = df['Sales Volume']
y_satisfaction = df['Customer Satisfaction']

# Create smooth lines using interpolation
x_new = np.linspace(x.min(), x.max(), 300)  # More points for smoothness
y_sales_smooth = make_interp_spline(x, y_sales, k=3)(x_new)
y_satisfaction_smooth = make_interp_spline(x, y_satisfaction, k=3)(x_new)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_new, y_sales_smooth, label='Sales Volume', color='blue')
plt.plot(x_new, y_satisfaction_smooth, label='Customer Satisfaction', color='green')

# Add titles and labels
plt.title('Smooth Line Chart of Sales Volume and Customer Satisfaction by Product ID')
plt.xlabel('Product ID')
plt.ylabel('Value')
plt.legend()

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a DataFrame with your data
data = {
    'Product ID': [1, 2, 3, 4, 5],
    'Sales Volume': [10, 12, 38, 30, 32],
    'Customer Satisfaction': [12, 4, 20, 15, 50]
}

df = pd.DataFrame(data)

# Set up the bar chart
x = np.arange(len(df['Product ID']))  # The label locations
width = 0.35  # The width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars for Sales Volume
bars1 = ax.bar(x - width/2, df['Sales Volume'], width, label='Sales Volume', color='blue')

# Plot bars for Customer Satisfaction
bars2 = ax.bar(x + width/2, df['Customer Satisfaction'], width, label='Customer Satisfaction', color='green')

# Add titles and labels
ax.set_title('Bar Chart of Sales Volume and Customer Satisfaction by Product ID')
ax.set_xlabel('Product ID')
ax.set_ylabel('Value')
ax.set_xticks(x)
ax.set_xticklabels(df['Product ID'])
ax.legend()

# Show the plot
plt.show()

