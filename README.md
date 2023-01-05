# dbt_databricks_demo
Demo of using DBT on databricks with SQL and Python models

## Directories

* e2 - the DBT demo project
* slides - presentation slides created with jupyter

## Setup

In order to authenticate and connect to databricks, create the file `~/.dbt/profiles.yml` with content:

```yaml
e2:
  target: dev
  outputs:
    dev:
      type: databricks
      catalog: hive_metastore
      schema: _dbt_tmp
      host: {{YOUR_HOST}}
      http_path: {{CLUSTER_PATH}}
      threads: 1
      token: {{SECRET_TOKEN}}
```

Some notes regarding `http_path`:

* https://github.com/databricks/dbt-databricks#choosing-compute-for-a-python-model
* https://docs.databricks.com/partners/prep/dbt.html#step-2-create-a-dbt-project-and-specify-and-test-connection-settings

Complete the setup with by:
```
pip install -r requirements.txt
cd e2
dbt debug
```
