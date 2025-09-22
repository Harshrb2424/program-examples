import pandas as pd
import numpy as np
import os

# ----------------------------
# Step 1: Load the dataset from 'Customers.csv'
# ----------------------------
# Make sure 'Customers.csv' is in the same directory as this script
# Or provide the full path

# Option 1: If file is in current directory
file_path = 'Customers.csv'

# Uncomment below if file is elsewhere (adjust path accordingly)
# file_path = '/path/to/your/Customers.csv'

# Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found. Please check the file location.")

# Read CSV
df = pd.read_csv(file_path)

print("Original Dataset:")
print(df)
print("\n" + "="*60 + "\n")

# ----------------------------
# Optional: Data Cleaning (handle missing values)
# ----------------------------
# Fill missing Age with mean, Email with 'Unknown'
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Email'] = df['Email'].fillna('Unknown')

# Convert Age to int after filling
df['Age'] = df['Age'].astype(int)

# ----------------------------
# 1. Horizontal Partitioning (Split into 2 equal parts)
# ----------------------------
n = len(df)
horiz_part1 = df.iloc[:n//2].copy()
horiz_part2 = df.iloc[n//2:].copy()

print("Horizontal Partition 1 (First Half):")
print(horiz_part1)
print("\nHorizontal Partition 2 (Second Half):")
print(horiz_part2)
print("\n" + "-"*50 + "\n")

# ----------------------------
# 2. Vertical Partitioning (Group by related columns)
# ----------------------------
vert_part1 = df[['Customer ID', 'Name', 'Email']].copy()  # Identity Info
vert_part2 = df[['Age', 'Location']].copy()               # Demographic Info

print("Vertical Partition 1 (Customer Info - ID, Name, Email):")
print(vert_part1)
print("\nVertical Partition 2 (Demographics - Age, Location):")
print(vert_part2)
print("\n" + "-"*50 + "\n")

# ----------------------------
# 3. Round Robin Partitioning (2 partitions)
# ----------------------------
round_robin_part1 = df.iloc[::2].copy()  # Rows 0, 2, 4, ...
round_robin_part2 = df.iloc[1::2].copy() # Rows 1, 3, 5, ...

print("Round Robin Partition 1 (Even-indexed Rows):")
print(round_robin_part1)
print("\nRound Robin Partition 2 (Odd-indexed Rows):")
print(round_robin_part2)
print("\n" + "-"*50 + "\n")

# ----------------------------
# 4. Hash-based Partitioning on 'Customer ID'
# Extract numeric part from Customer ID (e.g., C0065 → 65)
# Then use modulo 2 to assign partition
# ----------------------------
# Extract numbers from Customer ID
df['HashKey'] = df['Customer ID'].str.extract(r'(\d+)').astype(int)
df['Partition'] = df['HashKey'] % 2

hash_part1 = df[df['Partition'] == 0].drop(columns=['HashKey', 'Partition']).copy()
hash_part2 = df[df['Partition'] == 1].drop(columns=['HashKey', 'Partition']).copy()

print("Hash Partition 1 (Customer ID % 2 == 0):")
print(hash_part1)
print("\nHash Partition 2 (Customer ID % 2 == 1):")
print(hash_part2)