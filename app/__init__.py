from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import routes
from app.models.Game import Game
from app.models.GameCode import GameCode
from app.models.Setting import Setting  # Add this line