from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

import sqlalchemy as sql
from database_code.settings import *

app = Flask(__name__)

def connect_database():
    sql_conn = sql.create_engine(f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}").connect()

    return sql_conn

def load_jobs_from_database():
    connection = connect_database()
    jobs_sql = connection.execute(sql.text('SELECT * FROM jobs'))
    jobs = jobs_sql.all()
    print('jobs from database: ', jobs)
    return jobs

# Get the web page
@app.route("/")
def home():
    JOBS = load_jobs_from_database()
    return render_template("home.html", jobs = JOBS)

# Get the json data
@app.route("/jobs/<int:id>")
def job(id):
    job = None
    jobs = load_jobs_from_database()
    job = [j for j in jobs if j["id"] == id][0]
    return jsonify(job)

if __name__ == "__main__":
    app.run(debug=True)