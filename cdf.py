import pandas as pd
import numpy as np

df = pd.read_csv('marathon-data.csv')

# Step 1: Convert 'final' times from HH:MM:SS to total seconds for easier computation
df['final_seconds'] = pd.to_timedelta(df['final']).dt.total_seconds()

# Step 2: Sort the final times in ascending order
sorted_final_seconds = np.sort(df['final_seconds'])

# Step 3: Calc CDF for each time
# CDF value at each point = (num of data points below that point) divided (the total number of points)
cdf = np.arange(1, len(sorted_final_seconds)+1) / len(sorted_final_seconds)

# Plot the CDF
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(sorted_final_seconds, cdf, marker='.', linestyle='none')
plt.xlabel('Final Time in Seconds')
plt.ylabel('CDF')
plt.title('CDF of Marathon Final Times')
plt.grid(True)
plt.show()
