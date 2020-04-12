import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:rakib1602066@localhost/mydatabase")
db = scoped_session(sessionmaker(bind=engine))


def insert():
    f=open('flight.csv')
    reader = csv.reader(f)
    for region, destination, durretion in reader:
        db.execute("insert into flight(region, destination, durretion) values(:region,:destination,:durretion)", {"region":region, "destination":destination, "durretion":durretion})
    db.commit()


def main():
    insert()
    flights = db.execute("SELECT * from flight")
    for flight in flights:
        print(" flight {} : from {}  to {} and duretion is : {}".format(flight.id,flight.region,flight.destination,flight.durretion))
    db.commit()


if __name__ == "__main__":
    main()

