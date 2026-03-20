import pandas as pd

# load dataset (make sure the csv file is in the same directory)
try:
    df = pd.read_csv('customer_data.csv')
except FileNotFoundError:
    raise FileNotFoundError("customer_data.csv not found in workspace. Please ensure the file is present.")

# ensure required columns exist
required_cols = ['purchase', 'loan_default', 'churn', 'spending_score']
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise KeyError(f"Missing required columns in dataframe: {missing}")

# 1-- probability of purchase
purchase_probability = df['purchase'].mean()

print("Probability of Purchase:", purchase_probability)

# 2-- risk of loan default
loan_default_risk = df['loan_default'].mean()

print("Loan Default Risk:", loan_default_risk)

# 3-- customer churn probability
churn_probability = df['churn'].mean()
print("Customer Churn Probability:", churn_probability)

# 4-- conditional probability
high_spenders = df[df['spending_score'] > 70]

prob_purchase_high_spenders = high_spenders['purchase'].mean()

print("Probability of Purchase for High Spenders:", prob_purchase_high_spenders)

# 5-- risk table
risk_summary = {
    "Purchase Probability": df['purchase'].mean(),
    "Loan Default Risk": df['loan_default'].mean(),
    "Customer Churn Risk": df['churn'].mean()
}

print(risk_summary)
