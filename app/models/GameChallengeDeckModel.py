# This should mimic the GameChallengeDeckModel.java class in the GHS-Server project.
from app import db

class GameChallengeDeckModel(db.Model):
    __tablename__ = 'game_challenge_deck'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current = db.Column(db.Integer, nullable=False)
    finished = db.Column(db.Integer, nullable=False)
    keep = db.Column(db.List, nullable=False)
    cards = db.Column(db.List, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, current, finished, keep, cards, active):
        self.current = current
        self.finished = finished
        self.keep = keep
        self.cards = cards
        self.active = active

    def get_current(self):
        return self.current
    
    def set_current(self, current):
        self.current = current
    
    def get_finished(self):
        return self.finished
    
    def set_finished(self, finished):
        self.finished = finished
    
    def get_keep(self):
        return self.keep
    
    def set_keep(self, keep):
        self.keep = keep
        
    def get_cards(self):
        return self.cards
    
    def set_cards(self, cards):
        self.cards = cards
    
    def get_active(self):
        return self.active
    
    def set_active(self, active):
        self.active = active
