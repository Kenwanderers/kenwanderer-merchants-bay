# ScenarioFinish.py

from app import db
from app.models import GameScenarioModel, LootType, Identifier

class ScenarioFinish(db.Model):
    __tablename__ = 'scenario_finishes'

    id = db.Column(db.Integer, primary_key=True)
    conclusion = db.Column(GameScenarioModel, nullable=True)
    success = db.Column(db.Boolean, nullable=False)
    battle_goals = db.Column(db.List(db.Integer), nullable=True)
    collective_gold = db.Column(db.List(db.Integer), nullable=True)
    collective_resources = db.Column(db.List(db.Map(LootType, db.Integer)), nullable=True)
    items = db.Column(db.List(db.List(db.Integer)), nullable=True)
    choose_location = db.Column(db.String(255), nullable=True)
    choose_unlock_character = db.Column(db.String(255), nullable=True)
    challenges = db.Column(db.Integer, nullable=True)
    calender_section_manual = db.Column(db.List(db.Integer), nullable=True)
    calendar_section_manual = db.Column(db.List(db.Integer), nullable=True)
    random_item = db.Column(Identifier, nullable=True)
    random_item_index = db.Column(db.Integer, nullable=True)
    random_items = db.Column(db.List(Identifier), nullable=True)
    random_item_blueprints = db.Column(db.List(db.Integer), nullable=True)

    def __init__(self, conclusion=None, success=False, battle_goals=None, collective_gold=None, collective_resources=None, items=None, choose_location=None, choose_unlock_character=None, challenges=None, calender_section_manual=None, calendar_section_manual=None, random_item=None, random_item_index=None, random_items=None, random_item_blueprints=None):
        self.conclusion = conclusion
        self.success = success
        self.battle_goals = battle_goals
        self.collective_gold = collective_gold
        self.collective_resources = collective_resources
        self.items = items
        self.choose_location = choose_location
        self.choose_unlock_character = choose_unlock_character
        self.challenges = challenges
        self.calender_section_manual = calender_section_manual
        self.calendar_section_manual = calendar_section_manual
        self.random_item = random_item
        self.random_item_index = random_item_index
        self.random_items = random_items
        self.random_item_blueprints = random_item_blueprints

    def __repr__(self):
        return f'<ScenarioFinish {self.id}>'