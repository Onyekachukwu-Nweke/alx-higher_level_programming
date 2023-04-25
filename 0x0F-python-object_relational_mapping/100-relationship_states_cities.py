#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
Usage: ./100-relationship_states_cities.py <mysql username> /
                                    <mysql password> /
                                    <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def relationship():
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # To start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco")

    state.cities.append(city)
    session.add(state)
    session.commit()
    session.close()

if __name__ == "__main__":
    relationship()
