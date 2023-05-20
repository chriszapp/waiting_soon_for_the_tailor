import os
import mysql.connector

from settings import *
from database_structure import *
from data_for_database import JOBS

print("Connecting to database...")
print("DATABASE: " + DATABASE)

connection =  mysql.connector.connect(
  host = HOST,
  user = USERNAME,
  passwd= PASSWORD,
  db= DATABASE,
  autocommit = True,
  ssl_verify_cert = True,
  ssl_ca = "cacert.pem"
)

print(connection)
print("Database connected successfully!")

cursor = connection.cursor()

# Create the table
cursor.execute(create_table_jobs)
