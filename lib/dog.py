from models import Base, Dog
import ipdb


def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    return session.query(Dog).all()


def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name)
    return query.first()


def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id)
    return query.first()


def find_by_name_and_breed(session, name, breed):
    pass


def update_breed(session, dog, breed):
    pass
