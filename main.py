from flask import Flask, render_template, url_for, flash, redirect, request
import json # javascript

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
