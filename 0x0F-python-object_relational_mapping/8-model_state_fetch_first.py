#!/usr/bin/python3
""" List states object from database """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    url = f"mysql://{user_name}:{password}"
    url += f"@localhost:3306/{dbName}"
    engine = create_engine(url)
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(State).first()
    if not result:
        print("Nothing")
    else:
        print(f"{result.id}: {result.name}")
