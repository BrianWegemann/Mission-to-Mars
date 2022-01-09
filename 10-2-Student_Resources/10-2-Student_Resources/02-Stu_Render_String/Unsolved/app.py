# import necessary libraries
from flask import Flask, render_template
from werkzeug.exceptions import HTTPVersionNotSupported

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)
# @TODO:  Create a route and view function that takes in a string and renders index.html template
# CODE GOES HERE
name = "Flask"
hobby = "Coding"

@app.route('/')
def index():
    return render_template('index_html', name=name, hobby=hobby)


if __name__ == "__main__":
    app.run(debug=True)
