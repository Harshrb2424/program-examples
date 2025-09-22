import pandas as pd
import numpy as np

# Create dataset
data = {
    "EmpID": range(101, 126),
    "Name": [
        "Alice", "Bob", "Charlie", "David", "Eve",
        "Frank", "Grace", "Helen", "Ivy", "Jack",
        "Karen", "Leo", "Mona", "Nina", "Oscar",
        "Paul", "Queen", "Raj", "Sam", "Tina",
        "Uma", "Victor", "Wendy", "Xavier", "Yara"
    ],
    "Department": [
        "HR", "Finance", "IT", "IT", "Finance",
        "HR", "Finance", "IT", "Finance", "HR",
        "IT", "Finance", "HR", "Finance", "IT",
        "HR", "Finance", "Finance", "IT", "HR",
        "Finance", "IT", "Finance", "HR", "IT"
    ],
    "Salary": [
        35000, 45000, 60000, 50000, np.nan,
        42000, 39000, 70000, 48000, 41000,
        55000, 58000, 36000, np.nan, 47000,
        40000, 53000, 61000, 30000, 46000,
        49500, 72000, 39000, 38000, 51000
    ],
    "Experience(Years)": [
        1, 3, 7, 5, 2,
        4, 2, 10, 6, 3,
        8, 9, 1, 2, 6,
        3, 7, 12, 1, 5,
        4, 11, 2, 2, 8
    ]
}

# Save to CSV
df_raw = pd.DataFrame(data)
df_raw.to_csv("employees_raw.csv", index=False)

print("✅ employees_raw.csv created successfully with 25 rows.")