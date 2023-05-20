import os
import mysql.connector
from settings import *
from create_database import *

print("Connecting to database...")
print("HOST: " + HOST)
print("USERNAME: " + USERNAME)
print("PASSWORD: " + PASSWORD)
print("DATABASE: " + DATABASE)

connection =  mysql.connector.connect(
  host = HOST,
  user = USERNAME,
  passwd= PASSWORD,
  db= DATABASE,
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl_ca = {
    "ca": "/etc/ssl/cert.pem"
  }
)

print(connection)
print("Database connected successfully!")

cursor = connection.cursor()

# Create the table
cursor.execute(create_table_jobs)
