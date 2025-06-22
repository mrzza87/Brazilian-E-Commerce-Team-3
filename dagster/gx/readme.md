CLI implementation of GX for validating staging tables, dim tables and fact tables
that are loaded in BQ brazilian-e-commerce-team-3.BET_Team3 dataset.

To execute the GX validation of staging tables:
  ```bash
cd <your path>/dagster/dataset
python gx_table_validation.py
```

To execute the GX validation of dim and fact tables:
  ```bash
cd <your path>/dagster/dim
python gx_dim_fact_validation.py
```
