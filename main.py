from scripts.extract_customers import extract_customer_data
from scripts.transform_data import transform_data
from scripts.load_to_postgre import load_data_to_postgre


def run_pipeline():
    print("🚀 Starting ETL pipeline...")

    # extract data
    df = extract_customer_data("data/raw/customer_dirty_data.csv")
    print("Data extracted successfully !!!!")

    # transform data (data cleaning)
    df_clean = transform_data(df)

    # Load Data
    load_data_to_postgre(df_clean)

if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        print("Pipeline failed:", e)
