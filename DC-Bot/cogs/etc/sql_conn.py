import mysql.connector

from config import HOST, USER, PASSWORD, DB
## Only working when not using .env ##

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
