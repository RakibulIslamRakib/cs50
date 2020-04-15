from flask import Flask,request,render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app = Flask(__name__)
engine = create_engine("postgresql://postgres:rakib1602066@localhost/mydatabase")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flight")
    return render_template("index.html",flights=flights)


@app.route('/book',methods=["POST"])
def book():
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html",messes = "Invalid flight number")
    if db.execute("Select * from flight where id = :id",{"id":flight_id}).rowcount==0:
        return render_template("error.html",messes = "No such flight with that flight")
    db.execute("Insert into passengers(name,flight_id) values(:name,:flight_id)",{"name":name,"flight_id":flight_id})
    db.commit()
    return render_template("success.html")


@app.route('/flights')
def flights():
    flights = db.execute("Select * from flight").fetchall()
    return render_template("flights.html",flights=flights)


@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    flight = db.execute("Select * from flight where id =:id",{"id":flight_id}).fetchone()
    if flight is None:
        return render_template("error.html",messes="NO such flight")
    passengers = db.execute("Select * from passengers where flight_id =:flight_id",{"flight_id":flight_id}).fetchall()
    return render_template("flight.html",passengers=passengers,flight=flight)


if __name__ == '__main__':
    app.run()



'''
laout.html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{%block title%} {%endblock%}</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous">
    <meta charset="UTF-8">
</head>
<body>
<div class="container">
    {%block body%} {%endblock%}
</div>
</body>
</html>
'''



'''
index.html
{% extends "laout.html" %}

{% block title %}
    Flights
{% endblock %}

{% block body %}
    <h1>Book a Flight</h1>

    <form action="{{ url_for('book') }}" method="post">

        <div class="form-group">
            <select class="form-control" name="flight_id">
                {% for flight in flights %}
                    <option value="{{ flight.id }}">{{ flight.region}} to {{ flight.destination }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="form-group">
            <input class="form-control" name="name" placeholder="Passenger Name">
        </div>

        <div class="form-group">
            <button class="btn btn-primary">Book Flight</button>
        </div>

    </form>
{% endblock %}

'''



'''
error.html
{% extends "laout.html" %}
{%block heading%}<title>Error</title>{%endblock%}
{%block body%}
    {{ messes }}
{%endblock%}
'''


'''
success.html

{% extends "laout.html" %}
{%block heading%}<title>Success</title>{%endblock%}
{%block body%}
    <h1>
    you have successfully book your flight
    </h1>
{%endblock%}
'''


'''
flights.html
{% extends "laout.html" %}
{%block heading%}<title>Flights</title>{%endblock%}
{%block body%}
    <h1>
    All the flights are:<br>
    </h1>
    <ul>
    {% for flight in flights %}
        <li>
        <a href="{{ url_for('flight',flight_id = flight.id) }}">from {{flight.region }} to {{ flight.destination }}</a>
        </li>
    {% endfor %}
    </ul>
{%endblock%}

'''


'''
flight.html
{% extends "laout.html" %}
{%block heading%}<title>Flight</title>{%endblock%}
{%block body%}
    <h1>
    Flight deteils:<br>
    </h1>
    <ul>
        <li><h3>Region: {{ flight.region }}</h3></li>
        <li><h3>Destination: {{ flight.destination }}</h3></li>
        <li><h3>Duretion: {{ flight.durretion }}</h3></li>
    </ul>
    <ul>
    <h1>Passengers:</h1>
    {% for passenger in passengers %}
        <li>
        <h3>{{passenger.name  }}</h3>
        </li>
    {% else%}
        <li>
        <h3>No passenger</h3>
        </li>
    {% endfor %}
    </ul>
{%endblock%}
'''
