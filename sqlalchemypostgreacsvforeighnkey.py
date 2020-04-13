import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:rakib1602066@localhost/mydatabase")
db = scoped_session(sessionmaker(bind=engine))
'''
here two table:
flight(id,region,destination,durretion)
passenger(id,name,flight_id)
'''

def main():
    flight_id = int(input("Enter flight id : "))
    flight = db.execute("select region,destination,durretion from flight where id = :id",{"id":flight_id}).fetchone()

    if flight is None:
        print("No such flight")
        return
    passengers = db.execute("select name from passengers where flight_id = :flight_id",{"flight_id":flight_id}).fetchall()

    for passenger in passengers:
        print(passenger.name)
    if len(passengers)==0:
        print("No passenger for this flight")


if __name__ == "__main__":
    main()

