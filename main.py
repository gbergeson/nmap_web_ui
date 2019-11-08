from flask import Flask, render_template
from os import path

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/begin_scan")
def begin_scan():
    return render_template('begin_scan.html')

@app.route("/report")
def report():
    if path.exists('./templates/report.html'):
        return render_template('report.html')
    else:
        return render_template('sample_report.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)
