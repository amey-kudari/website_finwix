from flask import Flask, render_template, url_for, flash, redirect, request
import json # javascript

app = Flask(__name__)

# company, parent, agency, city, primary offense, pen-year, pen-amount
sdata = [
    ['abc', 'Inc', 'federal', '', '308', '2018', '$100'],
    ['abd', 'Inc', 'federal', '', '308', '2018', '$100'],
    ['abe', 'Inc', 'federal', '', '308', '2018', '$100'],
    ['abf', 'Inc', 'federal', '', '308', '2018', '$100'],
    ['abg', 'Inc', 'federal', '', '308', '2018', '$100']
]

@app.route("/")
def mainpage():
    return render_template("index.html")

@app.route("/data")
def gdata():
    return json.dumps(sdata)


if __name__ == '__main__':
    app.run(debug=True)
