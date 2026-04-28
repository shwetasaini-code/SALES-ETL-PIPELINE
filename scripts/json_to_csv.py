import pandas as pd

def json_to_csv():
  df = pd.read_json("data/raw/product.json")
  df.to_csv("data/raw/product.csv", index=False)
  print(df.head())

json_to_csv()
print("CSV created successfully")
