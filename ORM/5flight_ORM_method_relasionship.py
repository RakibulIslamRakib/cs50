#models.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Flight(db.Model):
    __tablename__="Flights"
    id = db.Column(db.Integer,primary_key=True)
    region = db.Column(db.String,nullable=False)
    destination = db.Column(db.String, nullable=False)
    durretion = db.Column(db.Integer, nullable=False)
    passengers =  db.relationship("Passenger",backtrack="flight",lazy=TRue)


class Passenger(db.Model):
    __tablename__ = "Passengers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer,db.ForeignKey("Flights.id"), nullable=False)
    
#app.py
from flask import Flask,request,render_template
from  models import *
import  csv

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'rakib1602066',
    'db': 'mydatabase',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#app.config["SQLALCHEMY_DATABASE_URL"]="postgresql://postgres:rakib1602066@localhost/mydatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html",flights=flights)



@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # Add passenger.
    flight.add_passenger(name)
    return render_template("success.html")


@app.route("/flights")
def flights():
    """List all flights."""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # Get all passengers.
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)



    
