from app import db

class AdditionalIdentifier(db.Model):
    __tablename__ = 'additional_identifiers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String, nullable=False)
    marker = db.Column(db.String, nullable=False)
    tags = db.Column(db.JSON, nullable=False)

    def __init__(self, type, marker, tags):
        self.type = type
        self.marker = marker
        self.tags = tags

    def __repr__(self):
        return f"<AdditionalIdentifier(id={self.id}, type={self.type}, marker={self.marker}, tags={self.tags})>"

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_marker(self):
        return self.id
    
    def set_marker(self, marker):
        self.marker = marker

    def get_tags(self):
        return self.tags

    def set_tags(self, tags):
        self.tags = tags
