from dagster import asset, AssetExecutionContext
import subprocess

# replace with actual directory for meltano run
@asset
def meltano_csv_to_bigquery(context: AssetExecutionContext):
    """Runs Meltano pipeline to move data from CSV to BigQuery."""
    try:
        result = subprocess.run(
            ["meltano", "run", "tap-csv", "target-bigquery"],
            cwd = "/Users/luikk/Brazilian-E-Commerce-Team-3-Org/Dagster/GX_Meltano_Test",
            check=True,
            capture_output=True,
            text=True
        )
        context.log.info(result.stdout)
    except subprocess.CalledProcessError as e:
        context.log.error(e.stderr)
        raise

@asset(deps=[meltano_csv_to_bigquery])
def GX_validate_meltano():
    """Runs GX validation after meltano"""
    try:
        subprocess.run(
            ["python", "gx_table_validation.py"], 
            cwd="/Users/luikk/Brazilian-E-Commerce-Team-3-Org/Dagster/gx/dataset",
            check=True
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"GX after Meltano run failed: {e}")

# Replace with actual directory for dbt run
@asset(deps=[GX_validate_meltano])
def dbt_run():
    """Runs dbt run"""
    try:
        subprocess.run(["dbt", "run", "--project-dir", "/Users/luikk/Brazilian-E-Commerce-Team-3-Org/Dagster/GX_DBT_Test"], 
                       check=True, 
                       cwd="/Users/luikk/Brazilian-E-Commerce-Team-3-Org/Dagster/GX_DBT_Test/"
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"DBT run failed: {e}")

@asset(deps=[dbt_run])
def GX_validate_dbt():
    """Runs GX validation after dbt"""
    try:
        subprocess.run(
            ["python", "gx_dim_fact_validation.py"], 
            cwd="/Users/luikk/Brazilian-E-Commerce-Team-3-Org/Dagster/gx/dim",
            check=True
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"GX after Meltano run failed: {e}")