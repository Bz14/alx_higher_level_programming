#!/usr/bin/python3
""" List city from database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    url = f"mysql://{user_name}:{password}"
    url += f"@localhost:3306/{dbName}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City).order_by(City.id).all()
    for row in result:
        state_name = (session.query(State)
                      .filter(row.state_id == State.id)
                      .first())
        if state_name:
            print(f"{state_name.name}: ({row.id}) {row.name}")
