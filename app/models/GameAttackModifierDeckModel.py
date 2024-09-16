# This should mimic the GameAttackModifierDeckModel.java class in the GHS-Server project.
from app import db

class GameAttackModifierDeckModel(db.Model):
    __tablename__ = 'game_attack_modifier_deck'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current = db.Column(db.Integer, nullable=False)
    cards = db.Column(db.List, nullable=False)
    disgarded = db.Column(db.List, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    lastVisible = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String, nullable=False)
    bb = db.Column(db.Boolean, nullable=False)

    def __init__(self, current, cards, disgarded, active, lastVisible, state, bb):
        self.current = current
        self.cards = cards
        self.disgarded = disgarded
        self.active = active
        self.lastVisible = lastVisible
        self.state = state
        self.bb = bb
        
    def get_current(self):
        return self.current
    
    def set_current(self, current):
        self.current = current
    
    def get_cards(self):
        return self.cards
    
    def set_cards(self, cards):
        self.cards = cards
    
    def get_disgarded(self):
        return self.disgarded
    
    def set_disgarded(self, disgarded):
        self.disgarded = disgarded
    
    def get_active(self):
        return self.active
    
    def set_active(self, active):
        self.active = active
    
    def get_lastVisible(self):
        return self.lastVisible
    
    def set_lastVisible(self, lastVisible):
        self.lastVisible = lastVisible
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
    
    def get_bb(self):
        return self.bb
    
    def set_bb(self, bb):
        self.bb = bb
