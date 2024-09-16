from app import db

class Setting(db.Model):
    __tablename__ = 'setting'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(100), nullable=False)

    def __init__(self, name, value):
        self.name = name
        self.value = value