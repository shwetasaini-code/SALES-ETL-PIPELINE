# For saving data directly on local machine
# DB_CONFIG = {
#     "user": "postgres",
#     "password": "admin",
#     "host": "host.docker.internal",
#     "port": "5432",
#     "database": "sales_db"
# }

# For saving data on docker
DB_CONFIG = {
    "user": "airflow",
    "password": "airflow",
    "host": "postgres",
    "port": "5432",
    "database": "airflow"
}