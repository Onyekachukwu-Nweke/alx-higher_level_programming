#!/usr/bin/python3
"""
Write a script that lists all State objects that contains "a" from
the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    search = argv[4]

    if search.__contains__('TRUNCATE' or 'FROM' or 'SELECT' or '*'):
        search = ''

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # To start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == search).first()

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
