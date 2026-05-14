from sqlalchemy import create_engine
from config.db_config import DB_CONFIG, LOCAL_DB_CONFIG


def get_engine():
    connection_string = (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    return create_engine(connection_string)


def local_engine():
    connection_string = (
        f"postgresql://{LOCAL_DB_CONFIG['user']}:{LOCAL_DB_CONFIG['password']}"
        f"@{LOCAL_DB_CONFIG['host']}:{LOCAL_DB_CONFIG['port']}/{LOCAL_DB_CONFIG['database']}"
    )
    return create_engine(connection_string)
