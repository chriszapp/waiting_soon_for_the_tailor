from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

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

# Get the web page
@app.route("/")
def home():
    return render_template("home.html", jobs = JOBS)

# Get the json data
@app.route("/jobs/<int:id>")
def job(id):
    job = None
    for j in JOBS:
        if j["id"] == id:
            job = j
    return jsonify(job)

if __name__ == "__main__":
    app.run(debug=True)