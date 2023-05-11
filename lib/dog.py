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
    return query.one()


def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id)
    return query.one()


def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name, Dog.breed == breed)
    return query.one()


def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id == dog.id).update(
        {Dog.breed: breed}, synchronize_session=False
    )
    session.commit()
