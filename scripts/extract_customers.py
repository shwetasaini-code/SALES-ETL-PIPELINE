import pandas as pd
import logging

def extract_customer_data(path):
    logging.info("Extracting customer data !!!")
    df = pd.read_csv(path)
    logging.info(f"Extracted {len(df)} rows ✅")
    return df