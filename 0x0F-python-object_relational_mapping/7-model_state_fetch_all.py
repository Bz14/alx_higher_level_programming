#!/usr/bin/python3
"""" List all states ordere by id """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d  = sys.argv[3]
    name = f'mysql+mysqldb://{u}:{p}@localhost:3306/{d}'
    engine = create_engine(name, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).order_by(States.id)
    for row in rows:
        print("{}: {}".format(row.id, row.name))
    session.close()
