import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample sales data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [1200, 1500, 1700, 1600, 2100, 2500]
}

df = pd.DataFrame(data)

# Display dataset
print(df)

# Calculate growth
df['Growth'] = df['Sales'].pct_change()

# Plot sales trend
plt.figure(figsize=(10,5))
plt.plot(df['Month'], df['Sales'], marker='o')

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.grid(True)

print("Average Sales:", np.mean(df['Sales']))

plt.show()
