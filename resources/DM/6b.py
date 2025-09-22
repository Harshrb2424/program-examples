import pandas as pd

# -------------------------------
# Step 1: Extract
# -------------------------------
df = pd.read_csv("aoi_raw.csv")
print("=== RAW DATA ===")
print(df)

# -------------------------------
# Step 2: Define Concept Hierarchies
# -------------------------------
city_to_state = {
    "Hyderabad": "Telangana",
    "Delhi": "Delhi",
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Chennai": "Tamil Nadu"
}

state_to_country = {
    "Telangana": "India",
    "Delhi": "India",
    "Maharashtra": "India",
    "Tamil Nadu": "India"
}

def generalize_age(age):
    if age <= 20:
        return "Teen"
    elif 21 <= age <= 30:
        return "Young"
    elif 31 <= age <= 40:
        return "Adult"
    else:
        return "Senior"

# -------------------------------
# Step 3: Apply AOI (Generalization)
# -------------------------------
df["State"] = df["City"].map(city_to_state)
df["Country"] = df["State"].map(state_to_country)
df["AgeGroup"] = df["Age"].apply(generalize_age)

# Drop detailed columns (low-level)
df_generalized = df.drop(columns=["City", "Age"])

print("\n=== GENERALIZED DATA (AOI Result) ===")
print(df_generalized)

# -------------------------------
# Step 4: Load/Save Result
# -------------------------------
df_generalized.to_csv("aoi_generalized.csv", index=False)
print("\n✅ Generalized data saved to 'aoi_generalized.csv'")