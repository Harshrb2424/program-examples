import pandas as pd

# Sample supermarket transactions (each row = transaction)
data = {
    "TID": range(1, 11),
    "Items": [
        "Milk,Bread,Butter",
        "Milk,Bread",
        "Milk,Diaper,Beer,Eggs",
        "Bread,Butter",
        "Milk,Bread,Diaper,Beer",
        "Milk,Bread,Diaper,Butter",
        "Beer,Diaper",
        "Milk,Bread,Butter,Eggs",
        "Milk,Bread,Diaper,Beer,Butter",
        "Bread,Diaper,Beer"
    ]
}

df = pd.DataFrame(data)
df.to_csv("transactions.csv", index=False)

print("✅ transactions.csv created successfully with 10 rows.")