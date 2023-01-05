def model(dbt, session):
    # this config doesn't work with python
    dbt.config(location_root="s3://foo/bar")

    df = dbt.ref("uszips")

    return df.filter(df.state_id == "CO")
