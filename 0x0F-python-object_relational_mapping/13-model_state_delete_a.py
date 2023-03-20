#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py <mysql username> /
                                    <mysql password> /
                                    <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # To start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    search = State.name.like('%a%')
    states = session.query(State).filter(search).order_by(State.id).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
