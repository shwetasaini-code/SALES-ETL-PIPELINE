import pandas as pd
from db.connection import get_engine
import logging

def load_data_to_postgre(df):
    logging.info("Saving customer data !!!")
    # DB connection
    try:
        engine = get_engine()

        # Insert into DB
        df.to_sql("customers", engine, if_exists='append', index=False)

        logging.info("Data loaded successfully into PostgreSQL ✅")
    except Exception as e:
        logging.info("Data Loading to Postgre failed.❌")
        raise e
