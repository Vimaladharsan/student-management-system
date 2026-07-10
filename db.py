import mariadb

def get_connection():
    return mariadb.connect(
        host="localhost",
        port=3307,  # MariaDB port
        user="root",
        password="root",
        database="sms_db"
    )
