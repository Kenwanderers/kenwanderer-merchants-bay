# LootDeck.py

from app import db
from app.models import Loot

class LootDeck(db.Model):
    __tablename__ = 'loot_decks'

    id = db.Column(db.Integer, primary_key=True)
    current = db.Column(db.Integer, nullable=False)
    cards = db.relationship('Loot', backref='loot_deck', lazy=True)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, current, cards, active):
        self.current = current
        self.cards = cards
        self.active = active

    def __repr__(self):
        return f'<LootDeck {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'current': self.current,
            'cards': [card.to_dict() for card in self.cards],
            'active': self.active
        }
    
    @staticmethod
    def from_dict(data):
        return LootDeck(
            current=data['current'],
            cards=[Loot.from_dict(card) for card in data['cards']],
            active=data['active']
        )