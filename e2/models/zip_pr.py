def model(dbt, session):
    dbt.config(
        submission_method="job_cluster",
        job_cluster_config={
            "spark_version": "11.3.x-scala2.12",
            "node_type_id": "i3.xlarge",
            "num_workers": 0,
            "spark_conf": {
                "spark.databricks.cluster.profile": "singleNode",
                "spark.master": "local[*, 4]",
            },
            "custom_tags": {"ResourceClass": "SingleNode"},
        },
    )

    df = dbt.ref("uszips")

    return df.filter(df.state_id == "PR")
