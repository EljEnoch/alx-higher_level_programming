#!/usr/bin/python3
"""
Adds the new object
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_obj = State(name='Louisiana')
    session.add(new_obj)
    session.commit()
    state = session.query(State).filter(State.name == 'Louisiana').first()

    print (state.id)

    session.close()
