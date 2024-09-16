# GameObjectiveEntityModel.py

from app import db
from app.models import GameObjectiveContainerModel, ConditionName

class GameObjectiveEntityModel(db.Model):
    __tablename__ = 'game_objective_entities'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    marker = db.Column(db.String(50))
    dead = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    dormant = db.Column(db.Boolean, nullable=False)
    revealed = db.Column(db.Boolean, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    max_health = db.Column(db.Integer, nullable=False)
    entity_conditions = db.relationship('GameEntityConditionModel', backref='game_objective_entity', lazy=True)
    immunities = db.Column(db.List(db.Enum(ConditionName)))
    markers = db.Column(db.List(db.String(50)))
    tags = db.Column(db.List(db.String(50)))
    shield = db.Column(db.String(50))
    shield_persistent = db.Column(db.String(50))
    retaliate = db.Column(db.List(db.String(50)))
    retaliate_persistent = db.Column(db.List(db.String(50)))

    def __init__(self, uuid, number, marker, dead, active, dormant, revealed, health, max_health, entity_conditions, immunities, markers, tags, shield, shield_persistent, retaliate, retaliate_persistent):
        self.uuid = uuid
        self.number = number
        self.marker = marker
        self.dead = dead
        self.active = active
        self.dormant = dormant
        self.revealed = revealed
        self.health = health
        self.max_health = max_health
        self.entity_conditions = entity_conditions
        self.immunities = immunities
        self.markers = markers
        self.tags = tags
        self.shield = shield
        self.shield_persistent = shield_persistent
        self.retaliate = retaliate
        self.retaliate_persistent = retaliate_persistent

    def __repr__(self):
        return f'<GameObjectiveEntityModel {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'number': self.number,
            'marker': self.marker,
            'dead': self.dead,
            'active': self.active,
            'dormant': self.dormant,
            'revealed': self.revealed,
            'health': self.health,
            'max_health': self.max_health,
            'entity_conditions': [entity.to_dict() for entity in self.entity_conditions],
            'immunities': [condition.name for condition in self.immunities],
            'markers': self.markers,
            'tags': self.tags,
            'shield': self.shield,
            'shield_persistent': self.shield_persistent,
            'retaliate': self.retaliate,
            'retaliate_persistent': self.retaliate_persistent
        }