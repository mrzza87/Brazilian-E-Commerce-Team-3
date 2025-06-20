from dagster import Definitions
from my_dagster_project.assets import meltano_csv_to_bigquery, GX_validate_meltano, dbt_run, GX_validate_dbt

defs = Definitions(
    assets=[meltano_csv_to_bigquery, GX_validate_meltano, dbt_run, GX_validate_dbt],
)