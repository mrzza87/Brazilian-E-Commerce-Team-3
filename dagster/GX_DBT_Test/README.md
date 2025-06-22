Welcome to your new dbt project!

### Using the starter project
This DBT configuration is dependent on the existence of <your BQ project id>.<your BQ dataset name>.customer_100 table.

#### Update /dagster/GX_DBT_Test/models/dim_customer_100.sql

Select data from <your BQ project id>.<your BQ dataset name>.customer_100 which was created by Meltano.

Current setting is lkk-dsai.GX_Meltano_Test.customer_100

```
# dim_customer_100.sql

SELECT *
FROM `<your BQ project id>.<your BQ dataset name>.customer_100`
LIMIT 100
```

#### Update profiles.yml with the following:

```# profiles.yml

GX_DBT_Test:
target: dev
outputs:
  dev:
    type: bigquery
    method: service-account
    project: <your BQ project id>
    dataset: <your BQ dataset name>
    threads: 1
    location: US
    keyfile: <your path>/<your BQ service account>.json
```
Run and test your DBT project

```bash
cd <your path>/dagster/GX_DBT_Test
dbt debug
dbt run
dbt test
dbt docs generate
dbt docs serve
```

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
