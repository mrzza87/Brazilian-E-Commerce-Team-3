from google.cloud import bigquery

client = bigquery.Client(project="brazilian-e-commerce-team-3")

table_id = "brazilian-e-commerce-team-3.BET_Team3.order_reviews"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
    write_disposition="WRITE_TRUNCATE",
)

with open("data/raw/cleaned_olist_order_reviews.csv", "rb") as f:
    load_job = client.load_table_from_file(f, table_id, job_config=job_config)

load_job.result()  # Wait for job to finish
print("✅ Upload done!")
