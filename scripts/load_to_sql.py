import pandas as pd
from sqlalchemy import create_engine
import os

# 💾 Using SQLite (easiest option) — will create ecommerce.db in your repo root
engine = create_engine('sqlite:///ecommerce.db')

# 📂 Path to the raw CSV files
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, '..', 'data', 'raw')


# 📊 CSV filenames and target table names
datasets = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "payments",
    "olist_order_reviews_dataset.csv": "reviews",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "product_category_name_translation.csv": "category_translation",
    "olist_geolocation_dataset.csv": "geolocation"
}

# 🚀 Load and insert CSVs into the database
for file_name, table_name in datasets.items():
    file_path = os.path.join(DATA_PATH, file_name)
    print(f"📥 Loading {file_name} into '{table_name}' table...")
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

print("✅ All tables loaded successfully into the database!")
