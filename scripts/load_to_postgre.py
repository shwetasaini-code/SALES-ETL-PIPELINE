import pandas as pd
from db.connection import get_engine

def load_data_to_postgre(df):
    # DB connection
    engine = get_engine()

    # Insert into DB
    df.to_sql("customers",engine,if_exists='replace', index=False)

    print("Data loaded successfully into PostgreSQL!")

