from flask import Flask, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)

engine = create_engine("sqlite:///flights.db")
connection = engine.connect()

@app.route("/")
def index():
    connection = engine.connect()
    result = connection.execute(text("SELECT * FROM flights"))
    flights = result.all()

    # flights = connection.execute(text("SELECT * FROM flights")).all()

    return render_template("index.html", flights=flights)