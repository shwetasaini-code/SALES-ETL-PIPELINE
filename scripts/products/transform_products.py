import logging 

def transform_products(df):
    logging.info("Data Cleaning Started !!!")
    
    df['rating_rate'] = df['rating'].apply(lambda x: x['rate'])
    df['rating_count'] = df['rating'].apply(lambda x: x['count'])
    df.drop(columns=['rating'], inplace=True)
    
    logging.info('Data cleaned successfully !! ✔️')
    return df