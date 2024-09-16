# GameObjectiveContainerModel.py

from app import db
from app.models import GameObjectiveEntityModel, ScenarioObjectiveIdentifier, AdditionalIdentifier

class GameObjectiveContainerModel(db.Model):
    __tablename__ = 'game_objective_containers'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50), nullable=False)
    marker = db.Column(db.String(50))
    title = db.Column(db.String(50))
    name = db.Column(db.String(50), nullable=False)
    escort = db.Column(db.Boolean, nullable=False)
    entities = db.relationship('GameObjectiveEntityModel', backref='game_objective_container', lazy=True)
    level = db.Column(db.Integer)
    off = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    initiative = db.Column(db.Integer)
    objective_id = db.Column(db.Enum(ScenarioObjectiveIdentifier))
    additional_objective_id = db.Column(db.Enum(AdditionalIdentifier))
    
    def __repr__(self):
        return f'<GameObjectiveContainerModel {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'marker': self.marker,
            'title': self.title,
            'name': self.name,
            'escort': self.escort,
            'entities': [entity.to_dict() for entity in self.entities],
            'level': self.level,
            'off': self.off,
            'active': self.active,
            'health': self.health,
            'initiative': self.initiative,
            'objective_id': self.objective_id,
            'additional_objective_id': self.additional_objective_id
        }