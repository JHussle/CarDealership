import mysql.connector, os
from mysql.connector import connect 
def returnConnection():
    conn = connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )
    return conn
