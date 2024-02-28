import pandas as pd
import numpy as np
from util import to_minutes

df = pd.read_csv('marathon-data.csv')

# Step 1: Create a new dataframe which includes only males
df_males = df.loc[df['gender'] == 'M'].copy()

# Step 2: Convert final times from HH:MM:SS to total seconds for easier computation
df_males['final_minutes'] = df_males['final'].apply(to_minutes)

# Step 3: Sort the final times in ascending order
sorted_final_minutes = np.sort(df_males['final_minutes'])

# Step 4: Calc CDF for each time
# CDF value at each point = (num of data points below that point) divided (the total number of points)
cdf = np.arange(1, len(sorted_final_minutes)+1) / len(sorted_final_minutes)

# Plot the CDF
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(sorted_final_minutes, cdf, marker='.', linestyle='none')
plt.xlabel('Final Time in Minutes')
plt.ylabel('CDF')
plt.title('CDF of Marathon Final Times for Males')
plt.grid(True)
plt.show()
