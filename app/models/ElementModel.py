from app import db

class ElementModel(db.Model):
    __tablename__ = "element"
    type = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)

    def __init__(self, type, state):
        self.type = type
        self.state = state
        
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_state(self):
        return self.state
        
    def set_state(self, state):
        self.state = state
