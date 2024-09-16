# ScenarioRuleIdentifier.py

from app import db

class ScenarioRuleIdentifier(db.Model):
    __tablename__ = 'scenario_rule_identifiers'

    id = db.Column(db.Integer, primary_key=True)
    edition = db.Column(db.String(50), nullable=False)
    scenario = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    index = db.Column(db.Integer, nullable=False)
    section = db.Column(db.Boolean, nullable=False)

    def __init__(self, edition, scenario, group, index, section):
        self.edition = edition
        self.scenario = scenario
        self.group = group
        self.index = index
        self.section = section

    def __repr__(self):
        return f'<ScenarioRuleIdentifier {self.id}>'