#!/usr/bin/python3
"""
Write a script that inserts a State objects into
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

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # To start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    print(louisiana.id)
    session.close()
