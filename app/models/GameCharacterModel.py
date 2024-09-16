# This should mimic the GameCharacterModel.java class in the GHS-Server project.
import json
from app import db
from app.models import CharacterProgress, GameAttackModifierDeckModel, ConditionName, Identifier, GameEntityConditionModel, GameSummonModel

class GameCharacterModel(db.Model):
    __tablename__ = 'game_character'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    edition = db.Column(db.String, nullable=False)
    marker = db.Column(db.Boolean, nullable=False)
    title = db.Column(db.String, nullable=False)
    initiative = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    loot = db.Column(db.Integer, nullable=False)
    loot_cards = db.Column(db.List(db.Integer), nullable=False)
    treasures = db.Column(db.List(db.String), nullable=False)
    exhausted = db.Column(db.Boolean, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    off = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    max_health = db.Column(db.Integer, nullable=False)
    entity_conditions = db.Column(db.List(GameEntityConditionModel), nullable=False)
    immunities = db.Column(db.List(ConditionName), nullable=False)
    markers = db.Column(db.List(db.String), nullable=False)
    tags = db.Column(db.List(db.String), nullable=False)
    identity = db.Column(db.Integer, nullable=False)
    summons = db.Column(db.List(GameSummonModel), nullable=False)
    progress = db.Column(db.Enum(CharacterProgress), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    attack_modifier_deck = db.Column(db.Enum(GameAttackModifierDeckModel), nullable=False)
    donations = db.Column(db.Integer, nullable=False)
    token = db.Column(db.Integer, nullable=False)
    token_values = db.Column(db.List(db.Integer), nullable=False)
    absent = db.Column(db.Boolean, nullable=False)
    long_rest = db.Column(db.Boolean, nullable=False)
    battle_goals = db.Column(db.List(Identifier), nullable=False)
    battle_goal = db.Column(db.Boolean, nullable=False)
    shield = db.Column(db.String, nullable=False)
    shield_persistent = db.Column(db.String, nullable=False)
    retaliate = db.Column(db.List(db.String), nullable=False)
    retaliate_persistent = db.Column(db.List(db.String), nullable=False)

    def __init__(self, name, edition, marker, title, initiative, experience, loot, loot_cards, treasures, exhausted, level, off, active, health, max_health, entity_conditions, immunities, markers, tags, identity, summons, progress, number, attack_modifier_deck, donations, token, token_values, absent, long_rest, battle_goals, battle_goal, shield, shield_persistent, retaliate, retaliate_persistent):
        self.name = name
        self.edition = edition
        self.marker = marker
        self.title = title
        self.initiative = initiative
        self.experience = experience
        self.loot = loot
        self.loot_cards = loot_cards
        self.treasures = treasures
        self.exhausted = exhausted
        self.level = level
        self.off = off
        self.active = active
        self.health = health
        self.max_health = max_health
        self.entity_conditions = entity_conditions
        self.immunities = immunities
        self.markers = markers
        self.tags = tags
        self.identity = identity
        self.summons = summons
        self.progress = progress
        self.number = number
        self.attack_modifier_deck = attack_modifier_deck
        self.donations = donations
        self.token = token
        self.token_values = token_values
        self.absent = absent
        self.long_rest = long_rest
        self.battle_goals = battle_goals
        self.battle_goal = battle_goal
        self.shield = shield
        self.shield_persistent = shield_persistent
        self.retaliate = retaliate
        self.retaliate_persistent = retaliate_persistent

    def __repr__(self):
        return f'<GameCharacterModel {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'edition': self.edition,
            'marker': self.marker,
            'title': self.title,
            'initiative': self.initiative,
            'experience': self.experience,
            'loot': self.loot,
            'loot_cards': self.loot_cards,
            'treasures': self.treasures,
            'exhausted': self.exhausted,
            'level': self.level,
            'off': self.off,
            'active': self.active,
            'health': self.health,
            'max_health': self.max_health,
            'entity_conditions': self.entity_conditions,
            'immunities': self.immunities,
            'markers': self.markers,
            'tags': self.tags,
            'identity': self.identity,
            'summons': self.summons,
            'progress': self.progress,
            'number': self.number,
            'attack_modifier_deck': self.attack_modifier_deck,
            'donations': self.donations,
            'token': self.token,
            'token_values': self.token_values,
            'absent': self.absent,
            'long_rest': self.long_rest,
            'battle_goals': self.battle_goals,
            'battle_goal': self.battle_goal,
            'shield': self.shield,
            'shield_persistent': self.shield_persistent,
            'retaliate': self.retaliate,
            'retaliate_persistent': self.retaliate_persistent
        }
    
    def from_dict(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def from_json(self, json_str):
        data = json.loads(json_str)
        self.from_dict(data)

    def from_json_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.from_dict(data)

    def save_to_json_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.to_dict(), file)