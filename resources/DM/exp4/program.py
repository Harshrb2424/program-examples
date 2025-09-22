import pandas as pd
import numpy as np

# ---------------------------
# Step 1: Load dataset from CSV
# ---------------------------
df = pd.read_csv("sales_data.csv")
print("Original Data:")
print(df)

# ---------------------------
# Step 2: Construct a data cube using pivot_table
# ---------------------------
cube = pd.pivot_table(df, values="Sales",
                      index=["Product", "Region"],
                      columns=["Year", "Quarter"],
                      aggfunc=np.sum,
                      fill_value=0)

print("\nData Cube (Pivot Table):")
print(cube)

# ---------------------------
# Step 3: OLAP Operations
# ---------------------------

# 1. Roll-up (aggregate sales by Year only)
rollup = df.groupby("Year")["Sales"].sum()
print("\nRoll-up (Total Sales by Year):")
print(rollup)

# 2. Drill-down (breakdown of sales by Year and Quarter)
drilldown = df.groupby(["Year", "Quarter"])["Sales"].sum()
print("\nDrill-down (Sales by Year & Quarter):")
print(drilldown)

# 3. Slice (fix one dimension → only sales in Region='East')
slice_df = df[df["Region"] == "East"]
print("\nSlice (Sales in East Region):")
print(slice_df)

# 4. Dice (filter on multiple dimensions → Product='Laptop' and Year=2023)
dice_df = df[(df["Product"] == "Laptop") & (df["Year"] == 2023)]
print("\nDice (Laptop Sales in 2023):")
print(dice_df)

# 5. Pivot (reorient data → Products as rows, Region as columns)
pivot = pd.pivot_table(df, values="Sales", index="Product", columns="Region", aggfunc=np.sum)
print("\nPivot (Products vs Region):")
print(pivot)