import os

from flask import Flask, render_template, request
from model import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    for flight in Flight.query.filter_by(destination="New York"):
        print(f"Flight from {flight.origin} to {flight.destination} lasting: {flight.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()
