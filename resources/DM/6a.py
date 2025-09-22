import pandas as pd

# Sample dataset with attributes for generalization
data = {
    "StudentID": range(1, 11),
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve",
             "Frank", "Grace", "Helen", "Ivy", "Jack"],
    "City": ["Hyderabad", "Hyderabad", "Delhi", "Delhi", "Mumbai",
             "Pune", "Pune", "Chennai", "Chennai", "Hyderabad"],
    "Age": [21, 25, 19, 32, 45, 28, 22, 35, 41, 18],
    "Department": ["CSE", "CSE", "ECE", "ECE", "MECH",
                   "CSE", "EEE", "MECH", "EEE", "CSE"]
}

# Save to CSV
df_raw = pd.DataFrame(data)
df_raw.to_csv("aoi_raw.csv", index=False)

print("✅ aoi_raw.csv created successfully with 10 rows.")