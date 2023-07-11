from flask import Flask, render_template, request, url_for, flash, redirect
import csv
import uuid

app = Flask (__name__)
app.config['SECRET_KEY']= "senhasecreta123"

@app.route("/")
def homepage():
    return render_template("login.html")





if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)