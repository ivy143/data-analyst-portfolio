# creating a/b groups
import pandas as pd
import numpy as np

# load dataset using script-relative path
import os
script_dir = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.normpath(os.path.join(script_dir, '..', 'customer_data.csv'))
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    raise FileNotFoundError(f"customer_data.csv not found at {csv_path}. Adjust path if necessary.")

# ensure purchase column exists
if 'purchase' not in df.columns:
    raise KeyError("Column 'purchase' is required for A/B testing but not found in dataframe.")

# Create A/B experiment groups
df['experiment_group'] = np.random.choice(['A','B'], size=len(df))

#calculating purchase rates for each group
group_results = df.groupby('experiment_group')['purchase'].mean()

print(group_results)


# perform statistical test 
from scipy.stats import ttest_ind

groupA = df[df['experiment_group']=='A']['purchase']
groupB = df[df['experiment_group']=='B']['purchase']

t_stat, p_value = ttest_ind(groupA, groupB)

print("T-statistic:", t_stat)
print("P-value:", p_value)



