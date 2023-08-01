from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'New york, USA',
        'salary': '$100,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, USA',
        'salary': '$200,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': '$125,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Florida, USA',
        'salary': '$120,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html',
                           jobs=JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)