from app import db
from app.models.Game import Game
from app.models.GameCode import GameCode
from app.models.Setting import Setting

class GameService:
    @staticmethod
    def get_all_games():
        return Game.query.all()

    @staticmethod
    def get_game_by_id(game_id):
        return Game.query.get(game_id)

    @staticmethod
    def create_game(game_data):
        new_game = Game(game=game_data['game'])
        db.session.add(new_game)
        db.session.commit()
        return new_game

class GameCodeService:
    @staticmethod
    def get_all_game_codes():
        return GameCode.query.all()

    @staticmethod
    def get_game_code_by_id(code_id):
        return GameCode.query.get(code_id)

    @staticmethod
    def create_game_code(game_code_data):
        new_game_code = GameCode(code=game_code_data['code'], game_id=game_code_data['game_id'])
        db.session.add(new_game_code)
        db.session.commit()
        return new_game_code

class SettingService:
    @staticmethod
    def get_all_settings():
        return Setting.query.all()

    @staticmethod
    def get_setting_by_key(key):
        return Setting.query.filter_by(key=key).first()

    @staticmethod
    def create_or_update_setting(setting_data):
        setting = Setting.query.filter_by(key=setting_data['key']).first()
        if setting:
            setting.value = setting_data['value']
        else:
            setting = Setting(key=setting_data['key'], value=setting_data['value'])
            db.session.add(setting)
        db.session.commit()
        return setting

def add_setting(name, value):
    setting = Setting(name=name, value=value)
    db.session.add(setting)
    db.session.commit()