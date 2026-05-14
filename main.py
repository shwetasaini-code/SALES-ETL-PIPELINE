import logging
from scripts.products.extract_products_api import extract_products
from scripts.products.transform_products import transform_products
from scripts.products.load_product_to_postgre import load_data__to_local

logging.basicConfig(level=logging.INFO)


def run_pipeline():
    logging.info("🚀 Starting ETL pipeline...")

    # extract data
    df = extract_products()
    logging.info("Data extracted successfully !!!!")

    # transform data (data cleaning)
    df_clean = transform_products(df)

    # Load Data
    load_data__to_local(df_clean)


if __name__ == "__main__":
    try:
        run_pipeline()
        logging.info("✅ Process completed successfully.")
    except Exception as e:
        logging.error("❌ Pipeline failed:", e)
