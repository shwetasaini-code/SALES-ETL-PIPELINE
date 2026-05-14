# For saving data directly on local machine
LOCAL_DB_CONFIG = {
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432",
    "database": "sales_db"
}

# For saving data on airflow sever
DB_CONFIG = {
    "user": "airflow",
    "password": "airflow",
    "host": "postgres",
    # "host": "host.docker.internal", # to save data on local machine usinh airflow
    "port": "5432",
    "database": "airflow"
}