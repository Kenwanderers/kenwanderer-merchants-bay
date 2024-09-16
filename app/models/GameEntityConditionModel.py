# GameEntityConditionModel.py

from app import db
from app.models.ConditionName import ConditionName
from app.models.EntityConditionState import EntityConditionState

class GameEntityConditionModel(db.Model):
    __tablename__ = 'game_entity_conditions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(ConditionName, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    state = db.Column(EntityConditionState, nullable=False)
    last_state = db.Column(EntityConditionState, nullable=False)
    permanent = db.Column(db.Boolean, nullable=False)
    expired = db.Column(db.Boolean, nullable=False)
    highlight = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, value, state, last_state, permanent, expired, highlight):
        self.name = name
        self.value = value
        self.state = state
        self.last_state = last_state
        self.permanent = permanent
        self.expired = expired
        self.highlight = highlight

    def __repr__(self):
        return f'<GameEntityConditionModel {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'state': self.state,
            'last_state': self.last_state,
            'permanent': self.permanent,
            'expired': self.expired,
            'highlight': self.highlight
        }
    
    @staticmethod
    def from_dict(data):
        return GameEntityConditionModel(
            name=data['name'],
            value=data['value'],
            state=data['state'],
            last_state=data['last_state'],
            permanent=data['permanent'],
            expired=data['expired'],
            highlight=data['highlight']
        )
    