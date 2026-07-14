import pandas as pd

# ----------------------------------
# Load Dataset
# ----------------------------------

file_path = r"C:\Users\HP\OneDrive\Desktop\Projects\Customer-Retention-Intelligence-Platform\data\raw\WA_Fn-UseC_-Telco-Customer-Churn.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 50)

print("\nShape:")
print(df.shape)

print("\nChecking blank values in TotalCharges...")
blank_values = (df["TotalCharges"] == " ").sum()
print(f"Blank values: {blank_values}")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print("\nMissing values after conversion:")
print(df["TotalCharges"].isna().sum())

print("\nUpdated Data Types:")
print(df.dtypes)

# ----------------------------------
# Remove rows with missing TotalCharges
# ----------------------------------

df = df.dropna(subset=["TotalCharges"])

print("\nShape after removing missing values:")
print(df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum())

# ----------------------------------
# Save cleaned dataset
# ----------------------------------

output_path = r"C:\Users\HP\OneDrive\Desktop\Projects\Customer-Retention-Intelligence-Platform\data\processed\customer_churn_cleaned.csv"

df.to_csv(output_path, index=False)

print("\n✅ Cleaned dataset saved successfully!")
print(output_path)