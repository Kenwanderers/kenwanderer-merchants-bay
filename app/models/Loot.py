# Loot.py

from app import db
from app.models import LootType

class Loot(db.Model):
    __tablename__ = 'loot'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(LootType), nullable=False)
    value4P = db.Column(db.Integer, nullable=True)
    value3P = db.Column(db.Integer, nullable=True)
    value2P = db.Column(db.Integer, nullable=True)
    value = db.Column(db.String(255), nullable=True)
    enhancements = db.Column(db.Integer, nullable=False)
    card_id = db.Column(db.Integer, nullable=True)

    def __init__(self, type, value4P, value3P, value2P, value, enhancements, card_id):
        self.type = type
        self.value4P = value4P
        self.value3P = value3P
        self.value2P = value2P
        self.value = value
        self.enhancements = enhancements
        self.card_id = card_id

    def __repr__(self):
        return f'<Loot {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'value4P': self.value4P,
            'value3P': self.value3P,
            'value2P': self.value2P,
            'value': self.value,
            'enhancements': self.enhancements,
            'card_id': self.card_id
        }
    
    @staticmethod
    def from_dict(data):
        return Loot(
            type=data['type'],
            value4P=data['value4P'],
            value3P=data['value3P'],
            value2P=data['value2P'],
            value=data['value'],
            enhancements=data['enhancements'],
            card_id=data['card_id']
        )