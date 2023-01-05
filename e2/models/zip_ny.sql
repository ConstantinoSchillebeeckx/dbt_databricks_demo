-- by default work is submitted as an "execution context" to either a SQLWarehouse cluster or an all-purpose cluster
-- here we change the default so that the model is executed as a notebook
{{ config(create_notebook=True) }}

SELECT *
FROM {{ ref('uszips') }}
WHERE state_id = "NY"
