from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:rakib1602066@localhost/mydatabase")
#username:postgres,password:r........6,databasename:mydatabase
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute("SELECT * from flight")
    for flight in flights:
        print("{} : {}".format(flight.id,flight.name))


if __name__ == "__main__":
    main()

