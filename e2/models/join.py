def model(dbt, session):

    df_co = dbt.ref("zip_co")
    df_pr = dbt.ref("zip_pr")

    return df_co.union(df_pr)
