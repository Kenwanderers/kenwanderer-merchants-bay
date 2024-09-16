from app import db

class GameCode(db.Model):
    __tablename__ = 'game_codes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String, unique=True, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)

    # Relationship with Game model
    game = db.relationship("Game", back_populates="codes")

    def __init__(self, code, game_id):
        self.code = code
        self.game_id = game_id

    def __repr__(self):
        return f"<GameCode(id={self.id}, code={self.code}, game_id={self.game_id})>"

    # Getter methods
    def get_id(self):
        return self.id

    def get_code(self):
        return self.code

    def get_game_id(self):
        return self.game_id

    # Setter methods
    def set_id(self, id):
        self.id = id

    def set_code(self, code):
        self.code = code

    def set_game_id(self, game_id):
        self.game_id = game_id