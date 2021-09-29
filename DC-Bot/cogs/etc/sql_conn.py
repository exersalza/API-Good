import mysql.connector

from config import HOST, USER, PASSWORD, DB


try:
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB
    )

    CUR = db.cursor()

except Exception:
    print(Exception)
