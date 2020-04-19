from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Flights(db.Model):
    __tablename__="Flights"
    id = db.Column(db.Integer,primary_key=True)
    region = db.Column(db.String,nullable=False)
    destination = db.Column(db.String, nullable=False)
    durretion = db.Column(db.Integer, nullable=False)


class Passengers(db.Model):
    __tablename__ = "Passengers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer,db.ForeignKey("Flights.id"), primary_key=True)
