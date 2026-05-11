from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.extract_customers import extract_customer_data
from scripts.transform_data import transform_data
from scripts.load_to_postgre import load_data_to_postgre
import pandas as pd
import logging

RAW_FILE = 'data/raw/customer_dirty_data.csv'
CLEAN_FILE = 'data/processed/customer_clean_data.csv'

logging.basicConfig(level=logging.INFO)

def extract_data_task():
    extract_customer_data(RAW_FILE)

def transform_data_task():
    df = pd.read_csv(RAW_FILE)
    transform_data(df)

def load_data_task():
    df_clean = pd.read_csv(CLEAN_FILE)
    load_data_to_postgre(df_clean)

default_args = {
    "owner": "Shweta",
    "retries": 3,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id='sales_etl_pipeline',
    description='Running ETL pipeline for sales',
    default_args=default_args,
    start_date=datetime(2026, 5, 10),
    schedule="@daily",
    catchup=False
) as dag:
    extract = PythonOperator(
        task_id="extract_data_task",
        python_callable=extract_data_task,
    )
    transform = PythonOperator(
        task_id="transform_data_task",
        python_callable=transform_data_task,
    )
    load = PythonOperator(
        task_id="load_data_task",
        python_callable=load_data_task,
    )

    extract >> transform >> load
