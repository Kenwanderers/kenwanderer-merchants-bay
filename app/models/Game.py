from app import db

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game = db.Column(db.String)

    # Relationship with GameCode model
    codes = db.relationship("GameCode", back_populates="game")

    def __init__(self, game):
        self.game = game

    def __repr__(self):
        return f"<Game(id={self.id}, game={self.game})>"

    # Getter methods
    def get_id(self):
        return self.id

    def get_game(self):
        return self.game

    # Setter methods
    def set_id(self, id):
        self.id = id

    def set_game(self, game):
        self.game = game
