import requests
import json
import os
import pandas as pd
import logging

base_url = 'https://fakestoreapi.com/products'


def extract_products():
    data = fetch_data()
    save_data_as_json(data)
    df = json_to_csv()
    return df


def fetch_data():
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception as e:
        logging('failed to retrieve data', e)
        raise e


def save_data_as_json(data):
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/product.json", "w") as f:
        json.dump(data, f, indent=4)


def json_to_csv():
    df = pd.read_json("data/raw/product.json")
    df.to_csv("data/raw/product.csv", index=False)
    return df
