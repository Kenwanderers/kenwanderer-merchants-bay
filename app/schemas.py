from app import ma
from app.models import Game, GameCode, Setting, Party, CharacterProgress, ScenarioFinish

class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        include_relationships = True
        load_instance = True
        dump_only = ('id',)

class GameCodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GameCode
        include_relationships = True
        load_instance = True
        dump_only = ('id',)

class SettingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Setting
        include_relationships = True
        load_instance = True
        dump_only = ('id',)

class PartySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Party
        include_relationships = True
        load_instance = True
        dump_only = ('id',)

class CharacterProgressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CharacterProgress
        include_relationships = True
        load_instance = True
        dump_only = ('id',)

class ScenarioFinishSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ScenarioFinish
        include_relationships = True
        load_instance = True
        dump_only = ('id',)

game_schema = GameSchema()
games_schema = GameSchema(many=True)
game_code_schema = GameCodeSchema()
game_codes_schema = GameCodeSchema(many=True)
setting_schema = SettingSchema()
settings_schema = SettingSchema(many=True)
party_schema = PartySchema()
parties_schema = PartySchema(many=True)
character_progress_schema = CharacterProgressSchema()
character_progresses_schema = CharacterProgressSchema(many=True)
scenario_finish_schema = ScenarioFinishSchema()
scenario_finishes_schema = ScenarioFinishSchema(many=True)