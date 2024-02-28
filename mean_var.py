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
data['final_minutes'] = data['final'].apply(to_minutes)

# Define quartiles and IQR
Q1 = data['final_minutes'].quantile(0.25)
Q3 = data['final_minutes'].quantile(0.75)
IQR = Q3 - Q1

# Set range for outliers as 1.5 times the IQR from the quartiles
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = data[(data['final_minutes'] < lower_bound) | (data['final_minutes'] > upper_bound)]

# Data without outliers
data_no_outliers = data[(data['final_minutes'] >= lower_bound) & (data['final_minutes'] <= upper_bound)].copy()

#Calculate mean with, without outliers
mean_with_outliers = np.mean(data['final_minutes'])
mean_without_outliers = np.mean(data_no_outliers['final_minutes'])

#Calulate median with, without outliers
median_with_outliers = np.median(data['final_minutes'])
median_without_outliers = np.median(data_no_outliers['final_minutes'])

# Calculate variance with, without outliers
variance_with_outliers = np.var(data['final_minutes'], ddof=1)  # ddof=1 for sample variance
variance_without_outliers = np.var(data_no_outliers['final_minutes'], ddof=1)

#Calculate standard deviation with, without outliers
std_dev_with_outliers = np.std(data['final_minutes'], ddof=1)  # ddof=1 for sample standard deviation
std_dev_without_outliers = np.std(data_no_outliers['final_minutes'], ddof=1)

print(variance_with_outliers, variance_without_outliers, mean_with_outliers, mean_without_outliers, median_with_outliers, median_without_outliers)

print(std_dev_with_outliers, std_dev_without_outliers)
