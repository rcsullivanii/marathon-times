import pandas as pd
import numpy as np
from util import to_minutes

df = pd.read_csv('marathon-data.csv')

# Step 1: Convert final times from HH:MM:SS to total seconds for easier computation
df['final_minutes'] = df['final'].apply(to_minutes)

# Step 2: Sort the final times in ascending order
sorted_final_minutes = np.sort(df['final_minutes'])

# Step 3: Calc CDF for each time
# CDF value at each point = (num of data points below that point) / (the total number of points)
cdf = np.arange(1, len(sorted_final_minutes)+1) / len(sorted_final_minutes)

# Plot the CDF
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(sorted_final_minutes, cdf, marker='.', linestyle='none')
plt.xlabel('Final Time in Minutes')
plt.ylabel('CDF')
plt.title('CDF of Marathon Final Times')
plt.grid(True)
plt.show()
