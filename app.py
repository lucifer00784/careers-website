from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru,India',
  'salary': 'RS.1,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi,India',
  'salary': 'RS.10,00,000'
}, {
  'id': 3,
  'title': 'Frontend devloper',
  'location': 'Hyderabad,India',
  'salary': 'RS.7,00,000'
}, {
  'id': 4,
  'title': 'Backend Devloper',
  'location': 'Mumbai,India',
  'salary': 'RS.9,00,000'
}, {
  'id': 5,
  'title': 'Fullstack Developer',
  'location': 'Bengaluru,India',
  'salary': 'RS.15,00,000'
}]


@app.route("/")
def hello_bright():
  return render_template('home.html', jobs=JOBS, company_name='Bright')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
