import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

data = {
    "customer_id": range(1, n+1),
    
    "age": np.random.randint(18, 65, n),
    
    "income": np.random.randint(20000, 120000, n),
    
    "spending_score": np.random.randint(1, 100, n),
    
    "website_version": np.random.choice(["A", "B"], n),
    
    "purchase": np.random.choice([0,1], n, p=[0.94,0.06]),
    
    "loan_default": np.random.choice([0,1], n, p=[0.9,0.1]),
    
    "churn": np.random.choice([0,1], n, p=[0.8,0.2])
}

df = pd.DataFrame(data)

df.to_csv("customer_data.csv", index=False)

print("Dataset created successfully!")
print(df.head())