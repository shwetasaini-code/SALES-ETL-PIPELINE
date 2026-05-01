import pandas as pd

def extract_customer_data(path):
    df = pd.read_csv(path)
    return df