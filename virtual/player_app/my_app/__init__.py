from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse\\application.db'
db = SQLAlchemy(app)
api = Api(app)

from my_app.player.views import player
app.register_blueprint(player)

db.create_all()
