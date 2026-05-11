import pandas as pd
from db.connection import get_engine


def load_data_to_postgre(df):
    # DB connection
    try:
        engine = get_engine()

        # Insert into DB
        df.to_sql("customers", engine, if_exists='append', index=False)

        print("Data loaded successfully into PostgreSQL !!!!")
    except Exception as e:
        print("Data Loading to Postgre failed.")
        raise e 