# GameScenarioModel.py

from app import db
from app.models import GameObjectiveContainerModel

class GameScenarioModel(db.Model):
    __tablename__ = 'game_scenarios'

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String(10), nullable=False)
    edition = db.Column(db.String(10), nullable=False)
    group = db.Column(db.String(10), nullable=True)
    is_custom = db.Column(db.Boolean, nullable=False)
    custom = db.Column(db.String(10), nullable=True)
    revealed_rooms = db.Column(db.List(db.Integer), nullable=False)

    def __init__(self, index, edition, group, is_custom, custom, revealed_rooms):
        self.index = index
        self.edition = edition
        self.group = group
        self.is_custom = is_custom
        self.custom = custom
        self.revealed_rooms = revealed_rooms

    def to_dict(self):
        return {
            'id': self.id,
            'index': self.index,
            'edition': self.edition,
            'group': self.group,
            'is_custom': self.is_custom,
            'custom': self.custom,
            'revealed_rooms': self.revealed_rooms
        }
