# Party.py

from app import db
from app.models import Identifier, GameScenarioModel, LootType, GameAttackModifierDeckModel, BuildingModel, CountIdentifier, GameCharacterModel, ConditionName, Loot

class Party(db.Model):
    __tablename__ = 'parties'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    edition = db.Column(db.String(50), nullable=False)
    conditions = db.relationship('ConditionName', backref='party', lazy=True)
    battle_goal_editions = db.Column(db.String(255), nullable=True)
    filtered_battle_goals = db.Column(db.List(Identifier), nullable=True)
    location = db.Column(db.String(255), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    achievements = db.Column(db.Text, nullable=True)
    achievements_list = db.Column(db.List(db.String), nullable=True)
    reputation = db.Column(db.Integer, nullable=True)
    prosperity = db.Column(db.Integer, nullable=True)
    scenarios = db.Column(db.List(GameScenarioModel), nullable=True)
    conclusions = db.Column(db.List(GameScenarioModel), nullable=True)
    casual_scenarios = db.Column(db.List(GameScenarioModel), nullable=True)
    manual_scenarios = db.Column(db.List(GameScenarioModel), nullable=True)
    campaign_mode = db.Column(db.Boolean, nullable=True)
    global_achievements = db.Column(db.Text, nullable=True)
    global_achievements_list = db.Column(db.List(db.String), nullable=True)
    treasures = db.Column(db.List(Identifier), nullable=True)
    donations = db.Column(db.Integer, nullable=True)
    players = db.Column(db.List(db.String), nullable=True)
    characters = db.Column(db.List(GameCharacterModel), nullable=True)
    available_characters = db.Column(db.List(GameCharacterModel), nullable=True)
    available_characters_list = db.Column(db.List(db.String), nullable=True)
    retirements = db.Column(db.List(GameCharacterModel), nullable=True)
    unlocked_items = db.Column(db.List(CountIdentifier), nullable=True)
    unlocked_characters = db.Column(db.List(db.String), nullable=True)
    level = db.Column(db.Integer, nullable=True)
    level_calculation = db.Column(db.Boolean, nullable=True)
    level_adjustment = db.Column(db.Integer, nullable=True)
    bonus_adjustment = db.Column(db.Integer, nullable=True)
    ge5_player = db.Column(db.Boolean, nullable=True)
    player_count = db.Column(db.Integer, nullable=True)
    solo = db.Column(db.Boolean, nullable=True)
    weeks = db.Column(db.Integer, nullable=True)
    week_sections = db.Column(db.Map(db.Integer, db.List(db.String)), nullable=True)
    loot = db.Column(db.Map(LootType, db.Integer), nullable=True)
    random_item_looted = db.Column(db.List(GameScenarioModel), nullable=True)
    inspiration = db.Column(db.Integer, nullable=True)
    defense = db.Column(db.Integer, nullable=True)
    soldiers = db.Column(db.Integer, nullable=True)
    morale = db.Column(db.Integer, nullable=True)
    town_guard_perks = db.Column(db.Integer, nullable=True)
    town_guard_perk_sections = db.Column(db.List(db.String), nullable=True)
    campaign_stickers = db.Column(db.List(db.String), nullable=True)
    town_guard_deck = db.Column(GameAttackModifierDeckModel, nullable=True)
    buildings = db.Column(db.List(BuildingModel), nullable=True)
    loot_deck_enhancements = db.Column(db.List(Loot), nullable=True)
    loot_deck_fixed = db.Column(db.List(LootType), nullable=True)
    loot_deck_sections = db.Column(db.List(db.String), nullable=True)
    envelope_b = db.Column(db.Boolean, nullable=True)

    def __init__(self, name, edition, conditions, battle_goal_editions, filtered_battle_goals, location, notes, achievements, achievements_list, reputation, prosperity, scenarios, conclusions, casual_scenarios, manual_scenarios, campaign_mode, global_achievements, global_achievements_list, treasures, donations, players, characters, available_characters, available_characters_list, retirements, unlocked_items, unlocked_characters, level, level_calculation, level_adjustment, bonus_adjustment, ge5_player, player_count, solo, weeks, week_sections, loot, random_item_looted, inspiration, defense, soldiers, morale, town_guard_perks, town_guard_perk_sections, campaign_stickers, town_guard_deck, buildings, loot_deck_enhancements, loot_deck_fixed, loot_deck_sections, envelope_b):
        self.name = name
        self.edition = edition
        self.conditions = conditions
        self.battle_goal_editions = battle_goal_editions
        self.filtered_battle_goals = filtered_battle_goals
        self.location = location
        self.notes = notes
        self.achievements = achievements
        self.achievements_list = achievements_list
        self.reputation = reputation
        self.prosperity = prosperity
        self.scenarios = scenarios
        self.conclusions = conclusions
        self.casual_scenarios = casual_scenarios
        self.manual_scenarios = manual_scenarios
        self.campaign_mode = campaign_mode
        self.global_achievements = global_achievements
        self.global_achievements_list = global_achievements_list
        self.treasures = treasures
        self.donations = donations
        self.players = players
        self.characters = characters
        self.available_characters = available_characters
        self.available_characters_list = available_characters_list
        self.retirements = retirements
        self.unlocked_items = unlocked_items
        self.unlocked_characters = unlocked_characters
        self.level = level
        self.level_calculation = level_calculation
        self.level_adjustment = level_adjustment
        self.bonus_adjustment = bonus_adjustment
        self.ge5_player = ge5_player
        self.player_count = player_count
        self.solo = solo
        self.weeks = weeks
        self.week_sections = week_sections
        self.loot = loot
        self.random_item_looted = random_item_looted
        self.inspiration = inspiration
        self.defense = defense
        self.soldiers = soldiers
        self.morale = morale
        self.town_guard_perks = town_guard_perks
        self.town_guard_perk_sections = town_guard_perk_sections
        self.campaign_stickers = campaign_stickers
        self.town_guard_deck = town_guard_deck
        self.buildings = buildings
        self.loot_deck_enhancements = loot_deck_enhancements
        self.loot_deck_fixed = loot_deck_fixed
        self.loot_deck_sections = loot_deck_sections
        self.envelope_b = envelope_b

    def __repr__(self):
        return f'<Party {self.name}>'