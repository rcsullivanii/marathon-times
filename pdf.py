import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm
import pandas as pd
import numpy as np

from util import to_minutes

# Load the data
data_path = 'marathon-data.csv'
data = pd.read_csv(data_path)

# Convert the final time to seconds
data['to_minutes'] = data['final'].apply(to_minutes)

# Define quartiles and IQR
Q1 = data['to_minutes'].quantile(0.25)
Q3 = data['to_minutes'].quantile(0.75)
IQR = Q3 - Q1

# Set range for outliers as 1.5 times the IQR from the quartiles
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = data[(data['final_minutes'] < lower_bound) | (data['final_minutes'] > upper_bound)]

# Data without outliers
data_no_outliers = data[(data['final_minutes'] >= lower_bound) & (data['final_minutes'] <= upper_bound)].copy()

# Fit log-normal distribution to data
shape, loc, scale = lognorm.fit(data_no_outliers['final_minutes'], floc=0)

# Generate range of values for PDF
xmin, xmax = data_no_outliers['final_minutes'].min(), data_no_outliers['final_minutes'].max()
x = np.linspace(xmin, xmax, 1000)

# Generate the PDF for the log-normal distribution
pdf = lognorm.pdf(x, shape, loc, scale)

# Plot the distribution of final_minutes and the PDF
sns.histplot(data_no_outliers['final_minutes'], kde=False, stat='density', bins=50, label='Data Density')
plt.plot(x, pdf, 'r-', lw=2, label='Log-normal PDF')
plt.title('Distribution of Marathon Finishing Times')
plt.xlabel('Final Time (minutes)')
plt.ylabel('Density')
plt.legend()
plt.show()
