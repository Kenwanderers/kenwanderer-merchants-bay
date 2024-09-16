from flask import jsonify, request
from app import app
from app.services import GameService, GameCodeService, SettingService
from app.schemas import game_schema, games_schema, game_code_schema, game_codes_schema, setting_schema, settings_schema
from app.models.Setting import Setting
from app import db

@app.route('/api/games', methods=['GET'])
def get_games():
    games = GameService.get_all_games()
    return jsonify(games_schema.dump(games))

@app.route('/api/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = GameService.get_game_by_id(game_id)
    if game:
        return jsonify(game_schema.dump(game))
    return jsonify({'message': 'Game not found'}), 404

@app.route('/api/games', methods=['POST'])
def create_game():
    game_data = request.json
    new_game = GameService.create_game(game_data)
    return jsonify(game_schema.dump(new_game)), 201

@app.route('/api/game-codes', methods=['GET'])
def get_game_codes():
    game_codes = GameCodeService.get_all_game_codes()
    return jsonify(game_codes_schema.dump(game_codes))

@app.route('/api/game-codes/<int:code_id>', methods=['GET'])
def get_game_code(code_id):
    game_code = GameCodeService.get_game_code_by_id(code_id)
    if game_code:
        return jsonify(game_code_schema.dump(game_code))
    return jsonify({'message': 'Game code not found'}), 404

@app.route('/api/game-codes', methods=['POST'])
def create_game_code():
    game_code_data = request.json
    new_game_code = GameCodeService.create_game_code(game_code_data)
    return jsonify(game_code_schema.dump(new_game_code)), 201

@app.route('/api/settings', methods=['GET'])
def get_settings():
    settings = Setting.query.all()
    # Serialize and return settings
    return jsonify(settings_schema.dump(settings))

@app.route('/api/settings/<string:key>', methods=['GET'])
def get_setting(key):
    setting = SettingService.get_setting_by_key(key)
    if setting:
        return jsonify(setting_schema.dump(setting))
    return jsonify({'message': 'Setting not found'}), 404

@app.route('/api/settings', methods=['POST'])
def create_or_update_setting():
    setting_data = request.json
    setting = SettingService.create_or_update_setting(setting_data)
    return jsonify(setting_schema.dump(setting)), 201