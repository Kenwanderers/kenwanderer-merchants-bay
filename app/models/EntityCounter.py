from app import db

class EntityCounter(db.Model):
    __tablename__ = "entity_counter"
    identifier = db.Column(db.String, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    killed = db.Column(db.Integer, nullable=False)

    def __init__(self, identifier, total, killed):
        self.identifier = identifier
        self.total = total
        self.killed = killed

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_total(self):
        return self.total
        
    def set_total(self, total):
        self.total = total

    def get_killed(self):
        return self.killed

    def set_killed(self, killed):
        self.killed = killed
