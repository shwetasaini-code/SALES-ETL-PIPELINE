import requests
import json
import os

base_url = 'https://fakestoreapi.com/products'

def fetch_data():
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('failed to retrieve data')

def save_data_as_json(data):
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/product.json", "w") as f:
        json.dump(data, f, indent=4)

data = fetch_data()
# print(data)
save_data_as_json(data)
print(f"Records fetched: {len(data)}")