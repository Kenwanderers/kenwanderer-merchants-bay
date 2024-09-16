# ScenarioObjectiveIdentifier.py

from app import db

class ScenarioObjectiveIdentifier(db.Model):
    __tablename__ = 'scenario_objective_identifiers'

    id = db.Column(db.Integer, primary_key=True)
    edition = db.Column(db.String(50), nullable=False)
    scenario = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    section = db.Column(db.Boolean, nullable=False)
    index = db.Column(db.Integer, nullable=False)

    def __init__(self, edition, scenario, group, section, index):
        self.edition = edition
        self.scenario = scenario
        self.group = group
        self.section = section
        self.index = index

    def __repr__(self):
        return f'<ScenarioObjectiveIdentifier {self.id}>'
    