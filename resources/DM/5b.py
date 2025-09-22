import pandas as pd

# -------------------------------
# Step 1: Extract
# -------------------------------
df = pd.read_csv("employees_raw.csv")
print("=== RAW DATA (Extracted) ===")
print(df.head(10))

# -------------------------------
# Step 2: Transform
# -------------------------------

# Fill missing salary with mean
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# Standardize department names to uppercase
df["Department"] = df["Department"].str.upper()

# Filter rows with Salary > 40000
df_filtered = df[df["Salary"] > 40000]

# Add Experience Level column
df_filtered["ExperienceLevel"] = pd.cut(
    df_filtered["Experience(Years)"],
    bins=[0, 3, 7, 20],
    labels=["Junior", "Mid-level", "Senior"]
)

print("\n=== TRANSFORMED DATA ===")
print(df_filtered.head(10))

# -------------------------------
# Step 3: Load
# -------------------------------
df_filtered.to_csv("employees_clean.csv", index=False)

print("\n✅ Clean data has been saved to 'employees_clean.csv'")
print(f"Total Rows Before: {len(df)} | After Transformation: {len(df_filtered)}")
