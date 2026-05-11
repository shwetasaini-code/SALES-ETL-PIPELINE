import pandas as pd
import ast as ast
import os

def safe_parse(x):
    try:
        if pd.isna(x):
            return {}
        x = x.replace("null", "None")  # fix null
        return ast.literal_eval(x)
    except:
        return {}

def transform_data(df):

    # flatten rating column
    res = df["review_info"].apply(safe_parse)
    df["review_info_score"] = res.apply(lambda x: x['score'])
    df["review_info_reviews"] = res.apply(lambda x: x['reviews'])
    df.drop(columns=['review_info'], inplace=True)

    # clean strings
    df['name'] = df['name'].str.strip().str.title()
    df['email'] = df['email'].str.strip()
    df['city'] = df['city'].str.strip().str.title()

    # fixing format
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
    df["review_info_score"] = pd.to_numeric(
        df["review_info_score"], errors="coerce")
    df["review_info_reviews"] = pd.to_numeric(
        df["review_info_reviews"], errors="coerce")

    # Remove rows with missing review_info_score
    df.dropna(subset=['review_info_score'], inplace=True)

    # Fill missing city
    df["city"] = df["city"].fillna("Unknown")
    df.fillna({'salary': df['salary'].median()}, inplace=True)  # another way
    df.fillna({'review_info_reviews': 0}, inplace=True)
    df.fillna({'age': df['age'].median()}, inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # print(df[df.isna().any(axis=1)]) #to check row which will get deleted if empty
    # print(df[df['review_info_score'].isna()]) #to check row which will get deleted if empty for specific column

    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/customer_clean_data.csv', index=False)

    print("Data cleaning completed !!!!")
    return df