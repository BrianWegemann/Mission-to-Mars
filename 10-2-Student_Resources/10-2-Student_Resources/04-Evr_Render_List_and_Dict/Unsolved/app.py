# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)
# @TODO: Create a list of dictionaries
# CODE GOES HERE
@app.route('/')
dog_dict = [{"name":"Fido", "type":"Lab"}, {"name":"Marshall", "type":"Shepard"}, {"name": "Max", "type":"Retriever"}, {"name": "Lucy", "type": "Pug"}]
def index():
    return render_template('index.html', dog_dict=dog_dict)
# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
# CODE GOES HERE

if __name__ == "__main__":
    app.run(debug=True)
