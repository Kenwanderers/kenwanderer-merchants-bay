# GameSummonModel.py

from app import db
from app.models import GameEntityConditionModel, ConditionName, SummonState, SummonColor

class GameSummonModel(db.Model):
    __tablename__ = 'game_summons'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    card_id = db.Column(db.String(255), nullable=True)
    number = db.Column(db.Integer, nullable=False)
    color = db.Column(SummonColor, nullable=False)
    attack = db.Column(db.String(255), nullable=True)
    movement = db.Column(db.Integer, nullable=True)
    range = db.Column(db.Integer, nullable=True)
    flying = db.Column(db.Boolean, nullable=True)
    dead = db.Column(db.Boolean, nullable=True)
    state = db.Column(SummonState, nullable=False)
    level = db.Column(db.Integer, nullable=True)
    health = db.Column(db.Integer, nullable=False)
    max_health = db.Column(db.Integer, nullable=False)
    entity_conditions = db.relationship('GameEntityConditionModel', backref='game_summon', lazy=True)
    immunities = db.Column(db.List(ConditionName), nullable=True)
    markers = db.Column(db.List(db.String(255)), nullable=True)
    tags = db.Column(db.List(db.String(255)), nullable=True)
    action = db.Column(db.String(255), nullable=True)
    additional_action = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean, nullable=False)
    dormant = db.Column(db.Boolean, nullable=False)
    revealed = db.Column(db.Boolean, nullable=False)
    thumbnail = db.Column(db.String(255), nullable=True)
    thumbnail_url = db.Column(db.String(255), nullable=True)
    no_thumbnail = db.Column(db.Boolean, nullable=False)
    shield = db.Column(db.String(255), nullable=True)
    shield_persistent = db.Column(db.String(255), nullable=True)
    retaliate = db.Column(db.List(db.String(255)), nullable=True)
    retaliate_persistent = db.Column(db.List(db.String(255)), nullable=True)

    def __init__(self, uuid, name, title, card_id, number, color, attack, movement, range, flying, dead, state, level, health, max_health, entity_conditions, immunities, markers, tags, action, additional_action, active, dormant, revealed, thumbnail, thumbnail_url, no_thumbnail, shield, shield_persistent, retaliate, retaliate_persistent):
        self.uuid = uuid
        self.name = name
        self.title = title
        self.card_id = card_id
        self.number = number
        self.color = color
        self.attack = attack
        self.movement = movement
        self.range = range
        self.flying = flying
        self.dead = dead
        self.state = state
        self.level = level
        self.health = health
        self.max_health = max_health
        self.entity_conditions = entity_conditions
        self.immunities = immunities
        self.markers = markers
        self.tags = tags
        self.action = action
        self.additional_action = additional_action
        self.active = active
        self.dormant = dormant
        self.revealed = revealed
        self.thumbnail = thumbnail
        self.thumbnail_url = thumbnail_url
        self.no_thumbnail = no_thumbnail
        self.shield = shield
        self.shield_persistent = shield_persistent
        self.retaliate = retaliate
        self.retaliate_persistent = retaliate_persistent

    def __repr__(self):
        return f'<GameSummonModel {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'title': self.title,
            'card_id': self.card_id,
            'number': self.number,
            'color': self.color,
            'attack': self.attack,
            'movement': self.movement,
            'range': self.range,
            'flying': self.flying,
            'dead': self.dead,
            'state': self.state,
            'level': self.level,
            'health': self.health,
            'max_health': self.max_health,
            'entity_conditions': [condition.to_dict() for condition in self.entity_conditions],
            'immunities': self.immunities,
            'markers': self.markers,
            'tags': self.tags,
            'action': self.action,
            'additional_action': self.additional_action,
            'active': self.active,
            'dormant': self.dormant,
            'revealed': self.revealed,
            'thumbnail': self.thumbnail,
            'thumbnail_url': self.thumbnail_url,
            'no_thumbnail': self.no_thumbnail,
            'shield': self.shield,
            'shield_persistent': self.shield_persistent,
            'retaliate': self.retaliate,
            'retaliate_persistent': self.retaliate_persistent
        }