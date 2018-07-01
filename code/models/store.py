from db import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))

    items = relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': list(map(lambda x: x.json(), self.items.all()))}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id)
