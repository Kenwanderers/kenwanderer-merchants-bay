# GameMonsterModel.py

from app import db
from app.models import GameMonsterEntityModel

class GameMonsterModel(db.Model):
    __tablename__ = 'game_monsters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    edition = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    off = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    draw_extra = db.Column(db.Boolean, nullable=False)
    last_draw = db.Column(db.Integer, nullable=False)
    ability = db.Column(db.Integer, nullable=False)
    abilities = db.Column(db.List(db.Integer), nullable=False)
    entities = db.relationship('GameMonsterEntityModel', backref='game_monster', lazy=True)
    is_ally = db.Column(db.Boolean, nullable=False)
    is_allied = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, edition, level, off, active, draw_extra, last_draw, ability, abilities, entities, is_ally, is_allied):
        self.name = name
        self.edition = edition
        self.level = level
        self.off = off
        self.active = active
        self.draw_extra = draw_extra
        self.last_draw = last_draw
        self.ability = ability
        self.abilities = abilities
        self.entities = entities
        self.is_ally = is_ally
        self.is_allied = is_allied

    def __repr__(self):
        return f'<GameMonsterModel {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'edition': self.edition,
            'level': self.level,
            'off': self.off,
            'active': self.active,
            'draw_extra': self.draw_extra,
            'last_draw': self.last_draw,
            'ability': self.ability,
            'abilities': self.abilities,
            'entities': [entity.to_dict() for entity in self.entities],
            'is_ally': self.is_ally,
            'is_allied': self.is_allied
        }
    
    @staticmethod
    def from_dict(data):
        return GameMonsterModel(
            name=data['name'],
            edition=data['edition'],
            level=data['level'],
            off=data['off'],
            active=data['active'],
            draw_extra=data['draw_extra'],
            last_draw=data['last_draw'],
            ability=data['ability'],
            abilities=data['abilities'],
            entities=data['entities'],
            is_ally=data['is_ally'],
            is_allied=data['is_allied']
        )
