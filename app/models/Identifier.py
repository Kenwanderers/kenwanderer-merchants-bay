# Identifier.py

from app import db

class Identifier(db.Model):
    __tablename__ = 'identifiers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    edition = db.Column(db.String(255), nullable=False)

    def __init__(self, name, edition):
        self.name = name
        self.edition = edition

    def __repr__(self):
        return f'<Identifier {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'edition': self.edition
        }
    
    @staticmethod
    def from_dict(data):
        return Identifier(name=data['name'], edition=data['edition'])