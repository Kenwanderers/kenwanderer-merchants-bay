# GameMonsterEntityModel.py

from app import db
from app.models import MonsterType, SummonState, GameEntityConditionModel, ConditionName

class GameMonsterEntityModel(db.Model):
    __tablename__ = 'game_monster_entities'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    marker = db.Column(db.String(50))
    type = db.Column(db.Enum(MonsterType), nullable=False)
    dead = db.Column(db.Boolean, nullable=False)
    summon = db.Column(db.Enum(SummonState), nullable=False)
    revealed = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    dormant = db.Column(db.Boolean, nullable=False)
    off = db.Column(db.Boolean, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    max_health = db.Column(db.Integer, nullable=False)
    entity_conditions = db.relationship('GameEntityConditionModel', backref='game_monster_entity', lazy=True)
    immunities = db.Column(db.List(db.Enum(ConditionName)))
    markers = db.Column(db.List(db.String(50)))
    tags = db.Column(db.List(db.String(50)))
    shield = db.Column(db.String(50))
    shield_persistent = db.Column(db.String(50))
    retaliate = db.Column(db.List(db.String(50)))
    retaliate_persistent = db.Column(db.List(db.String(50)))

    def __init__(self, number, marker, type, dead, summon, revealed, active, dormant, off, health, max_health, entity_conditions, immunities, markers, tags, shield, shield_persistent, retaliate, retaliate_persistent):
        self.number = number
        self.marker = marker
        self.type = type
        self.dead = dead
        self.summon = summon
        self.revealed = revealed
        self.active = active
        self.dormant = dormant
        self.off = off
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