import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# -------------------------------
# Step 1: Extract
# -------------------------------
df = pd.read_csv("transactions.csv")
print("=== RAW TRANSACTIONS ===")
print(df)

# Convert "Items" column into list of lists
transactions = df["Items"].apply(lambda x: x.split(",")).tolist()

# -------------------------------
# Step 2: Transform (One-hot encoding)
# -------------------------------
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)

print("\n=== TRANSACTIONS ONE-HOT ENCODED ===")
print(df_trans.head())

# -------------------------------
# Step 3: Apply Apriori
# -------------------------------
frequent_itemsets = apriori(df_trans, min_support=0.3, use_colnames=True)

print("\n=== FREQUENT ITEMSETS (min_support=0.3) ===")
print(frequent_itemsets)

# -------------------------------
# Step 4: Generate Association Rules
# -------------------------------
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

print("\n=== ASSOCIATION RULES ===")
print(rules[["antecedents", "consequents", "support", "confidence", "lift"]])

# -------------------------------
# Step 5: Save Results
# -------------------------------
frequent_itemsets.to_csv("frequent_itemsets.csv", index=False)
rules.to_csv("association_rules.csv", index=False)

print("\n✅ Results saved to 'frequent_itemsets.csv' and 'association_rules.csv'")