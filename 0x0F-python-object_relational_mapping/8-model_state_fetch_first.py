#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    row = query.first()
    if (row is not None):
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
