Update the extractor and loader config in meltano.yml

Extractor (tap-csv): path to customer_100.csv
Loader (target-cvs): BQ project id, BQ dataset name, BQ JSON credentials of service account that can access BQ project and dataset.

```bash
cd <your path>/dagster/GX_Meltano_Test
meltano run tap-csv target-csv
```
