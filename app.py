# Importing flask module 
from flask import Flask
# Create an object of a Flask class
app = Flask(__name__)
# The route function of the flask class
@app.route("/")
def first_flask():
    return "This is my first flask program"


#run the application on local server
app.run()


# Define a function with different endpoint "flask_2"

@app.route("/flask_2")
def second_flask():
    return "Python is fun"

app.run(debug = True)

