from app import db

class CountIdentifier(db.Model):
    __tablename__ = "count_identifier"
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, count):
        self.count = count

    def __repr__(self):
        return f"<CountIdentifier(id={self.id}, count={self.count})>"

    def get_id(self):
        return self.id

    def get_count(self):
        return self.count

    def set_count(self, count):
        self.count = count
    