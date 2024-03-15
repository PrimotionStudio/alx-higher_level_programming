#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).join(State)
    .filter(City.state_id == State.id).order_by(City.id)
    print(query)
    for city, state in query.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
