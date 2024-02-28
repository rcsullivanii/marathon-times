import pandas as pd
import numpy as np

from util import to_minutes

# Load the data
data_path = 'marathon-data.csv'
data = pd.read_csv(data_path)

# Filter dataset for female runners 
female_data = data[data['gender'] == 'W']

# Calc 25th percentile for whole distribution
P25_time_overall = np.percentile(data['final_minutes'], 25)

# Probability of a female runner finishing under the 25th percentile of the overall distribution
P_A_and_B_female = female_data[female_data['final_minutes'] < P25_time_overall].shape[0] / female_data.shape[0]

# Probability of being a female runner in this dataset
P_B_female = female_data.shape[0] / data.shape[0]

# Conditional probability for female runners
P_A_given_B_female = P_A_and_B_female / P_B_female

P25_time_overall, P_A_and_B_female, P_B_female, P_A_given_B_female
