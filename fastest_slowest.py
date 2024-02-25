import pandas as pd
from datetime import timedelta

# Load data from CSV file into DataFrame
df = pd.read_csv('marathon-data.csv')

# Assuming 'split' and 'final' columns are in the format 'HH:MM:SS',
# convert these time strings to timedelta objects for comparison
df['split_timedelta'] = pd.to_timedelta('0 days ' + df['split'])
df['final_timedelta'] = pd.to_timedelta('0 days ' + df['final'])

# Find the row with the smallest 'final_timedelta', i.e., the fastest final time
fastest_final = df.loc[df['final_timedelta'].idxmin(), 'final']
slowest_final = df.loc[df['final_timedelta'].idxmax(), 'final']

print("The quickest finishing time is " + fastest_final)
print("The longest finishing time is " + slowest_final)