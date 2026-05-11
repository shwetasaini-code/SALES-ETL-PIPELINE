import logging
from scripts.extract_customers import extract_customer_data
from scripts.transform_data import transform_data
from scripts.load_to_postgre import load_data_to_postgre

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    logging.info("🚀 Starting ETL pipeline...")

    # extract data
    df = extract_customer_data("data/raw/customer_dirty_data.csv")
    logging.info("Data extracted successfully !!!!")

    # transform data (data cleaning)
    df_clean = transform_data(df)

    # Load Data
    load_data_to_postgre(df_clean)

if __name__ == "__main__":
    try:
        run_pipeline()
        logging.info("✅ Process completed successfully.")
    except Exception as e:
        logging.error("❌ Pipeline failed:", e)
         
