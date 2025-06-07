import pandas as pd
import csv
import re

# Step 1: Read CSV safely
df = pd.read_csv("data/raw/olist_order_reviews_dataset.csv", 
                 on_bad_lines='skip', 
                 dtype=str, 
                 encoding='utf-8')

# Step 2: Strip unwanted characters from each cell
def clean_cell(value):
    if pd.isna(value):
        return ""
    value = str(value)
    value = value.replace("\n", " ").replace("\r", " ")
    value = value.replace('"', "'")  # Replace double quotes
    value = re.sub(r'[^\x20-\x7E]', '', value)  # remove non-ASCII
    value = value.strip()
    return value

df = df.applymap(clean_cell)

# Step 3: Drop fully empty rows/columns
df.dropna(how="all", inplace=True)
df.dropna(axis=1, how="all", inplace=True)

# Step 4: Save cleaned CSV with safe quoting
df.to_csv("data/raw/cleaned_olist_order_reviews.csv", 
          index=False, 
          quoting=csv.QUOTE_ALL)  # quote everything

print("✅ Cleaned CSV saved as 'data/raw/cleaned_olist_order_reviews.csv'")
# Step 5: Check for duplicates and remove them
df.drop_duplicates(inplace=True)
# Step 6: Save cleaned CSV again after removing duplicates
df.to_csv("data/raw/cleaned_olist_order_reviews.csv", 
          index=False, 
          quoting=csv.QUOTE_ALL)  # quote everything
print("✅ Cleaned CSV with duplicates removed saved as 'data/raw/cleaned_olist_order_reviews.csv'")
# Step 7: Check for missing values and fill them with empty strings
df.fillna("", inplace=True)
# Step 8: Save final cleaned CSV
df.to_csv("data/raw/cleaned_olist_order_reviews.csv", 
          index=False, 
          quoting=csv.QUOTE_ALL)  # quote everything
print("✅ Final cleaned CSV saved as 'data/raw/cleaned_olist_order_reviews.csv'")
# Step 9: Print summary of cleaned data
print(f"✅ Cleaned data summary:")