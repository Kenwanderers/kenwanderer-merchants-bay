# Permissions.py

from app import db
from app.models import Identifier

class Permissions(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    characters = db.Column(db.Boolean, nullable=False)
    character = db.Column(db.List(Identifier), nullable=True)
    monsters = db.Column(db.Boolean, nullable=False)
    monster = db.Column(db.List(Identifier), nullable=True)
    scenario = db.Column(db.Boolean, nullable=False)
    elements = db.Column(db.Boolean, nullable=False)
    round = db.Column(db.Boolean, nullable=False)
    level = db.Column(db.Boolean, nullable=False)
    attack_modifiers = db.Column(db.Boolean, nullable=False)
    loot_deck = db.Column(db.Boolean, nullable=False)
    party = db.Column(db.Boolean, nullable=False)

    def __init__(self, characters=False, character=None, monsters=False, monster=None, scenario=False, elements=False, round=False, level=False, attack_modifiers=False, loot_deck=False, party=False):
        self.characters = characters
        self.character = character
        self.monsters = monsters
        self.monster = monster
        self.scenario = scenario
        self.elements = elements
        self.round = round
        self.level = level
        self.attack_modifiers = attack_modifiers
        self.loot_deck = loot_deck
        self.party = party

    def __repr__(self):
        return f'<Permissions {self.id}>'
