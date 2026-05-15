from db.connection import local_engine
import logging

def load_data__to_local(df_clean):
    logging.info("Saving products !!!")
    try:
        engine = local_engine()
        df_clean.to_sql('products', engine, if_exists='append', index=False)
        logging.info("Data loaded successfully into PostgreSQL ✅")

    except Exception as e:
        logging.info("Data Loading to Postgre failed.❌")
        raise e
