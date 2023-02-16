import mysql.connector
import os
import dotenv

connection = mysql.connector(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
)

cursor = connection.cursor()
