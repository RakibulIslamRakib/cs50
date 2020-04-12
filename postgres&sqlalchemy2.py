# simple insertion and deletion.
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:rakib1602066@localhost/mydatabase")
db = scoped_session(sessionmaker(bind=engine))


def insert():
    for i in range(5):
        name=input("Enter name : ")
        db.execute("insert into flight(name) values('{}')".format(name))
    db.commit()


def main():
    insert()
    flights = db.execute("SELECT * from flight")
    for flight in flights:
        print("{} : {}".format(flight.id,flight.name))

if __name__ == "__main__":
    main()

