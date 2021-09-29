import mysql.connector
from etc.config import HOST, USER, PASSWORD, DB

db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB
)

