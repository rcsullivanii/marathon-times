import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from util import to_minutes

# Load the data
data_path = 'marathon-data.csv'
data = pd.read_csv(data_path)

# Convert the final time to seconds
data['final_minutes'] = data['final'].apply(to_minutes)

# Generate a histogram for the final_minutes data 
plt.figure(figsize=(10, 6))
plt.hist(data['final_minutes'], bins=50, alpha=0.7, color='blue')
plt.title('Histogram of Marathon Final Times')
plt.xlabel('Final Time in Minutes')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

