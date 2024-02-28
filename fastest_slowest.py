import pandas as pd
from datetime import timedelta
from util import to_minutes

# Load data from CSV file into DataFrame
df = pd.read_csv('marathon-data.csv')

# Convert 'final' from these time strings to timedelta objects for comparison
df['final_timedelta'] = df['final'].apply(to_minutes)

# Find the row with the fastest final time
fastest_final = df.loc[df['final_timedelta'].idxmin(), 'final']
slowest_final = df.loc[df['final_timedelta'].idxmax(), 'final']

print("The quickest finishing time is " + fastest_final)
print("The longest finishing time is " + slowest_final)