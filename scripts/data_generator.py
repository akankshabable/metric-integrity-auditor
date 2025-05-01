import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Constants
n_rows = 60000
start_date = pd.to_datetime("2024-01-01")
end_date = pd.to_datetime("2024-06-30")
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Generate synthetic data
user_ids = np.arange(100000, 100000 + n_rows)
groups = np.random.choice(['control', 'treatment'], size=n_rows, p=[0.5, 0.5])
signup_dates = np.random.choice(date_range, size=n_rows)
device_types = np.random.choice(['mobile', 'desktop', 'tablet'], size=n_rows, p=[0.6, 0.3, 0.1])
regions = np.random.choice(['North America', 'Europe', 'Asia', 'South America'], size=n_rows)
experiment_ids = np.random.choice(['exp_101', 'exp_102', 'exp_103'], size=n_rows)

# Introduce flaw: treatment group conversion inflated slightly
base_conversion = 0.10
conversion_rate = np.where(groups == 'control',
                           np.random.binomial(1, base_conversion, size=n_rows),
                           np.random.binomial(1, base_conversion + 0.02, size=n_rows))

# Assemble into DataFrame
df = pd.DataFrame({
    'user_id': user_ids,
    'group': groups,
    'converted': conversion_rate,
    'signup_date': signup_dates,
    'device_type': device_types,
    'region': regions,
    'experiment_id': experiment_ids
})

# Shuffle dataset
df = df.sample(frac=1).reset_index(drop=True)

# Save to CSV
df.to_csv("data/simulated_ab_test_data.csv", index=False)

print("✅ File 'simulated_ab_test_data.csv' has been created with 60,000 rows.")
