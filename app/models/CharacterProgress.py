from app import db
from app.models import LootType

class CharacterProgress(db.Model):
    __tablename__ = 'character_progress'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    experience = db.Column(db.Integer, nullable=False)
    gold = db.Column(db.Integer, nullable=False)
    loot = db.Column(db.Map(LootType, db.Integer), nullable=False)
    item_notes = db.Column(db.String, nullable=False)
    items = db.Column(db.JSON, nullable=False)
    equipped_items = db.Column(db.JSON, nullable=False)
    personal_quest = db.Column(db.String, nullable=False)
    personal_quest_progress = db.Column(db.JSON, nullable=False)
    battle_goals = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String, nullable=False)
    retired = db.Column(db.Boolean, nullable=False)
    retirements = db.Column(db.Integer, nullable=False)
    extra_perks = db.Column(db.Integer, nullable=False)
    perks = db.Column(db.JSON, nullable=False)
    masteries = db.Column(db.JSON, nullable=False)
    donations = db.Column(db.Integer, nullable=False)

    def __init__(self, experience, gold, loot, item_notes, items, equipped_items, personal_quest, personal_quest_progress, battle_goals, notes, retired, retirements, extra_perks, perks, masteries, donations):
        self.experience = experience
        self.gold = gold
        self.loot = loot
        self.item_notes = item_notes
        self.items = items
        self.equipped_items = equipped_items
        self.personal_quest = personal_quest
        self.personal_quest_progress = personal_quest_progress
        self.battle_goals = battle_goals
        self.notes = notes
        self.retired = retired
        self.retirements = retirements
        self.extra_perks = extra_perks
        self.perks = perks
        self.masteries = masteries
        self.donations = donations

    def __repr__(self):
        return f"<CharacterProgress(id={self.id}, experience={self.experience}, gold={self.gold}, loot={self.loot}, item_notes={self.item_notes}, items={self.items}, equipped_items={self.equipped_items}, personal_quest={self.personal_quest}, personal_quest_progress={self.personal_quest_progress}, battle_goals={self.battle_goals}, notes={self.notes}, retired={self.retired}, retirements={self.retirements}, extra_perks={self.extra_perks}, perks={self.perks}, masteries={self.masteries}, donations={self.donations})>"
    
    def get_id(self):
        return self.id

    def get_experience(self):
        return self.experience

    def get_gold(self):
        return self.gold
    
    def get_loot(self):
        return self.loot

    def get_item_notes(self):
        return self.item_notes

    def get_items(self):
        return self.items
    def get_loot(self):
        return self.loot

    def get_equipped_items(self):
        return self.equipped_items

    def get_personal_quest(self):
        return self.personal_quest

    def get_personal_quest_progress(self):
        return self.loot
    
    def get_battle_goals(self):
        return self.battle_goals

    def get_notes(self):
        return self.notes

    def get_retired(self):
        return self.retired
    
    def get_retirements(self):
        return self.retirements

    def get_extra_perks(self):
        return self.extra_perks

    def get_perks(self):
        return self.perks
    
    def get_masteries(self):
        return self.masteries

    def get_donations(self):
        return self.donations

    def set_id(self, id):
        self.id = id

    def set_experience(self, experience):
        self.experience = experience

    def set_gold(self, gold):
        self.gold = gold

    def set_loot(self, loot):
        self.loot = loot

    def set_item_notes(self, item_notes):
        self.item_notes = item_notes

    def set_items(self, items):
        self.items = items

    def set_equipped_items(self, equipped_items):
        self.equipped_items = equipped_items

    def set_personal_quest(self, personal_quest):
        self.personal_quest = personal_quest

    def set_personal_quest_progress(self, personal_quest_progress):
        self.personal_quest_progress = personal_quest_progress

    def set_battle_goals(self, battle_goals):
        self.battle_goals = battle_goals

    def set_notes(self, notes):
        self.notes = notes

    def set_retired(self, retired):
        self.retired = retired

    def set_retirements(self, retirements):
        self.retirements = retirements

    def set_extra_perks(self, extra_perks):
        self.extra_perks = extra_perks

    def set_perks(self, perks):
        self.perks = perks

    def set_masteries(self, masteries):
        self.masteries = masteries

    def set_donations(self, donations):
        self.donations = donations
