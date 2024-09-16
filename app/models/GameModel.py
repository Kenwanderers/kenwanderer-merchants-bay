# GameModel.py

from app import db
from app.models.GameChallengeDeckModel import GameChallengeDeckModel
from app.models.GameClockTimestamp import GameClockTimestamp
from app.models.GameMonsterEntityModel import GameMonsterEntityModel
from app.models.GameEntityConditionModel import GameEntityConditionModel
from app.models.ConditionName import ConditionName
from app.models.LootDeck import LootDeck
from app.models.Loot import Loot
from app.models.LootType import LootType
from app.models.Party import Party
from app.models.ScenarioFinish import ScenarioFinish

class GameModel(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    revision = db.Column(db.Integer, nullable=False)
    revision_offset = db.Column(db.Integer, nullable=False)
    edition = db.Column(db.String(50), nullable=False)
    conditions = db.Column(db.String(50), nullable=False)
    battle_goal_editions = db.Column(db.String(50), nullable=False)
    filtered_battle_goals = db.Column(db.String(50), nullable=False)
    figures = db.Column(db.String(50), nullable=False)
    entities_counter = db.Column(db.String(50), nullable=False)
    characters = db.Column(db.String(50), nullable=False)
    monsters = db.Column(db.String(50), nullable=False)
    objective_containers = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    scenario = db.Column(db.String(50), nullable=False)
    sections = db.Column(db.String(50), nullable=False)
    scenario_rules = db.Column(db.String(50), nullable=False)
    applied_scenario_rules = db.Column(db.String(50), nullable=False)
    discarded_scenario_rules = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    level_calculation = db.Column(db.Boolean, nullable=False)
    level_adjustment = db.Column(db.Integer, nullable=False)
    bonus_adjustment = db.Column(db.Integer, nullable=False)
    ge5_player = db.Column(db.Boolean, nullable=False)
    player_count = db.Column(db.Integer, nullable=False)
    round = db.Column(db.Integer, nullable=False)
    round_resets = db.Column(db.List(db.Integer), nullable=False)
    round_resets_hidden = db.Column(db.List(db.Integer), nullable=False)
    play_seconds = db.Column(db.Integer, nullable=False)
    total_seconds = db.Column(db.Integer, nullable=False)
    monster_attack_modifier_deck = db.Column(GameAttackModifierDeckModel, nullable=False)
    ally_attack_modifier_deck = db.Column(GameAttackModifierDeckModel, nullable=False)
    element_board = db.Column(db.List(ElementModel), nullable=False)
    solo = db.Column(db.Boolean, nullable=False)
    party = db.Column(Party, nullable=False)
    parties = db.Column(db.List(Party), nullable=False)
    loot_deck = db.Column(LootDeck, nullable=False)
    loot_deck_enhancements = db.Column(db.List(Loot), nullable=False)
    loot_deck_fixed = db.Column(db.List(LootType), nullable=False)
    loot_deck_sections = db.Column(db.List(db.String), nullable=False)
    unlocked_characters = db.Column(db.List(db.String), nullable=False)
    server = db.Column(db.Boolean, nullable=False)
    finish = db.Column(ScenarioFinish, nullable=False)
    game_clock = db.Column(db.List(GameClockTimestamp), nullable=False)
    challenge_deck = db.Column(GameChallengeDeckModel, nullable=False)

    def __init__(self, revision, revision_offset, edition, conditions, battle_goal_editions, filtered_battle_goals, figures, entities_counter, characters, monsters, objective_containers, state, scenario, sections, scenario_rules, applied_scenario_rules, discarded_scenario_rules, level, level_calculation, level_adjustment, bonus_adjustment, ge5_player, player_count, round, round_resets, round_resets_hidden, play_seconds, total_seconds, monster_attack_modifier_deck, ally_attack_modifier_deck, element_board, solo, party, parties, loot_deck, loot_deck_enhancements, loot_deck_fixed, loot_deck_sections, unlocked_characters, server, finish, game_clock, challenge_deck):
        self.revision = revision
        self.revision_offset = revision_offset
        self.edition = edition
        self.conditions = conditions
        self.battle_goal_editions = battle_goal_editions
        self.filtered_battle_goals = filtered_battle_goals
        self.figures = figures
        self.entities_counter = entities_counter
        self.characters = characters
        self.monsters = monsters
        self.objective_containers = objective_containers
        self.state = state
        self.scenario = scenario
        self.sections = sections
        self.scenario_rules = scenario_rules
        self.applied_scenario_rules = applied_scenario_rules
        self.discarded_scenario_rules = discarded_scenario_rules
        self.level = level
        self.level_calculation = level_calculation
        self.level_adjustment = level_adjustment
        self.bonus_adjustment = bonus_adjustment
        self.ge5_player = ge5_player
        self.player_count = player_count
        self.round = round
        self.round_resets = round_resets
        self.round_resets_hidden = round_resets_hidden
        self.play_seconds = play_seconds
        self.total_seconds = total_seconds
        self.monster_attack_modifier_deck = monster_attack_modifier_deck
        self.ally_attack_modifier_deck = ally_attack_modifier_deck
        self.element_board = element_board
        self.solo = solo
        self.party = party
        self.parties = parties
        self.loot_deck = loot_deck
        self.loot_deck_enhancements = loot_deck_enhancements
        self.loot_deck_fixed = loot_deck_fixed
        self.loot_deck_sections = loot_deck_sections
        self.unlocked_characters = unlocked_characters
        self.server = server
        self.finish = finish
        self.game_clock = game_clock
        self.challenge_deck = challenge_deck

    def __repr__(self):
        return f'<GameModel {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'revision': self.revision,
            'revision_offset': self.revision_offset,
            'edition': self.edition,
            'conditions': self.conditions,
            'battle_goal_editions': self.battle_goal_editions,
            'filtered_battle_goals': self.filtered_battle_goals,
            'figures': self.figures,
            'entities_counter': self.entities_counter,
            'characters': self.characters,
            'monsters': self.monsters,
            'objective_containers': self.objective_containers,
            'state': self.state,
            'scenario': self.scenario,
            'sections': self.sections,
            'scenario_rules': self.scenario_rules,
            'applied_scenario_rules': self.applied_scenario_rules,
            'discarded_scenario_rules': self.discarded_scenario_rules,
            'level': self.level,
            'level_calculation': self.level_calculation,
            'level_adjustment': self.level_adjustment,
            'bonus_adjustment': self.bonus_adjustment,
            'ge5_player': self.ge5_player,
            'player_count': self.player_count,
            'round': self.round,
            'round_resets': self.round_resets,
            'round_resets_hidden': self.round_resets_hidden,
            'play_seconds': self.play_seconds,
            'total_seconds': self.total_seconds,
            'monster_attack_modifier_deck': self.monster_attack_modifier_deck,
            'ally_attack_modifier_deck': self.ally_attack_modifier_deck,
            'element_board': self.element_board,
            'solo': self.solo,
            'party': self.party,
            'parties': self.parties,
            'loot_deck': self.loot_deck,
            'loot_deck_enhancements': self.loot_deck_enhancements,
            'loot_deck_fixed': self.loot_deck_fixed,
            'loot_deck_sections': self.loot_deck_sections,
            'unlocked_characters': self.unlocked_characters,
            'server': self.server,
            'finish': self.finish,
            'game_clock': self.game_clock,
            'challenge_deck': self.challenge_deck
        }
    
    @staticmethod
    def from_dict(data):
        return GameModel(
            revision=data['revision'],
            revision_offset=data['revision_offset'],
            edition=data['edition'],
            conditions=data['conditions'],
            battle_goal_editions=data['battle_goal_editions'],
            filtered_battle_goals=data['filtered_battle_goals'],
            figures=data['figures'],
            entities_counter=data['entities_counter'],
            characters=data['characters'],
            monsters=data['monsters'],
            objective_containers=data['objective_containers'],
            state=data['state'],
            scenario=data['scenario'],
            sections=data['sections'],
            scenario_rules=data['scenario_rules'],
            applied_scenario_rules=data['applied_scenario_rules'],
            discarded_scenario_rules=data['discarded_scenario_rules'],
            level=data['level'],
            level_calculation=data['level_calculation'],
            level_adjustment=data['level_adjustment'],
            bonus_adjustment=data['bonus_adjustment'],
            ge5_player=data['ge5_player'],
            player_count=data['player_count'],
            round=data['round'],
            round_resets=data['round_resets'],
            round_resets_hidden=data['round_resets_hidden'],
            play_seconds=data['play_seconds'],
            total_seconds=data['total_seconds'],
            monster_attack_modifier_deck=data['monster_attack_modifier_deck'],
            ally_attack_modifier_deck=data['ally_attack_modifier_deck'],
            element_board=data['element_board'],
            solo=data['solo'],
            party=data['party'],
            parties=data['parties'],
            loot_deck=data['loot_deck'],
            loot_deck_enhancements=data['loot_deck_enhancements'],
            loot_deck_fixed=data['loot_deck_fixed'],
            loot_deck_sections=data['loot_deck_sections'],
            unlocked_characters=data['unlocked_characters'],
            server=data['server'],
            finish=data['finish'],
            game_clock=data['game_clock'],
            challenge_deck=data['challenge_deck']
        )
    