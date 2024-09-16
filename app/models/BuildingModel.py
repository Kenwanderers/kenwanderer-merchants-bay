from app import db

class BuildingModel(db.Model):
    __tablename__ = 'buildings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String, nullable=False)

    def __init__(self, name, level, state):
        self.name = name
        self.level = level
        self.state = state

    def __repr__(self):
        return f'<BuildingModel {self.name}>'
    
    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level

    def set_state(self, state):
        self.state = state

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_state(self):
        return self.state

    def get_id(self):
        return self.id
