import pandas as pd
import sqlalchemy as sql

from settings import *


JOBS = [
    {
        "id": 1,
        "title": "Software Engineer",
        "description": "A software engineer is a person who applies the principles of software engineering to the design, development, maintenance, testing, and evaluation of computer software.",
        "salary": "$100,000",
        "company": "Google",
        "email": "emailme@contactsomeoneelse.com"
    },

    {
        "id": 2,
        "title": "Data Engineer",
        "description": "A data engineer is a person who applies the principles of software engineering to the design, development, maintenance, testing, and evaluation of computer software.",
        "salary": "$100,000",
        "company": "Apple",
        "email": "emailme@contactsomeoneelse.com"
    },

    {
        "id": 3,
        "title": "Data Scientist",
        "description": "A data scientist is a person who applies the principles of software engineering to the design, development, maintenance, testing, and evaluation of computer software.",
        "salary": "$100,000",
        "company": "Notion",
        "email": "emailme@contactsomeoneelse.com"
    },
]

print('Connecting to database...')
sql_conn = sql.create_engine(f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}")

print(sql_conn)

print('Loading data into database...')
jobs_df = pd.DataFrame(JOBS)
print(jobs_df.head())

print('Writing data to database...')
jobs_df.to_sql("jobs", sql_conn, if_exists="replace", index=False)

print('Done!')