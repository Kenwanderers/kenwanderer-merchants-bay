# GameClockTimestamp.py

from app import db

class GameClockTimestamp(db.Model):
    __tablename__ = 'game_clock_timestamps'

    id = db.Column(db.Integer, primary_key=True)
    clock_in = db.Column(db.DateTime, nullable=False)
    clock_out = db.Column(db.DateTime, nullable=True)

    def __init__(self, clock_in, clock_out):
        self.clock_in = clock_in
        self.clock_out = clock_out

    def __repr__(self):
        return f'<GameClockTimestamp {self.id}>'
    
    def get_clock_in(self):
        return self.clock_in
    
    def get_clock_out(self):
        return self.clock_out
    
    def set_clock_in(self, clock_in):
        self.clock_in = clock_in
        
    def set_clock_out(self, clock_out):
        self.clock_out = clock_out