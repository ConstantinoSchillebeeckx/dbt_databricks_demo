def model(dbt, session):
    # location_root doesn't work with python
    dbt.config(location_root="s3://foo/bar", create_notebook=True)

    df = dbt.ref("uszips")

    return df.filter(df.state_id == "CO")
