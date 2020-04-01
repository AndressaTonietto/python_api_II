import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.player.models import Player
from my_app import api, db

player = Blueprint('player',__name__)

parser = reqparse.RequestParser()
parser.add_argument('name',type=str)
parser.add_argument('nickname',type=str)
parser.add_argument('team',type=str)
parser.add_argument('role',type=str)
parser.add_argument('kills',type=int)
parser.add_argument('assists',type=int)
parser.add_argument('deaths',type=int)
parser.add_argument('totalGames',type=int)
parser.add_argument('wins',type=int)

@player.route("/")
@player.route("/home")
def home():
  return "Catálogo de Jogadores"

class PlayerAPI(Resource):
  def get(self,id=None,page=1):
    if not id:
      players = Player.query.paginate(page,10).items
    else:
      players = [Player.query.get(id)]
    if not players:
      abort(404)
    res = {}
    for p in players:
      res[p.id] = {
        'name': p.name,
        'nickname': p.nickname,
        'team': p.team,
        'role': p.role,
        'kills': p.kills,
        'assists': p.assists,
        'deaths': p.deaths,
        'totalGames': p.totalGames,
        'wins': p.wins,
        'KDA': str(p.kills+p.assists) if (p.deaths == 0) else str((p.kills+p.assists)/p.deaths),
        'winRate': p.wins/p.totalGames*100,
      }
    return json.dumps(res)

  def post(self):
    args = parser.parse_args()
    name = args['name']
    nickname = args['nickname']
    team = args['team']
    role = args['role']
    kills = args['kills']
    assists = args['assists']
    deaths = args['deaths']
    totalGames = args['totalGames']
    wins = args['wins']

    p = Player(name,nickname,team,role,kills,assists,deaths,totalGames,wins)
    db.session.add(p)
    db.session.commit()
    res = {}
    res[p.id] = {
      'name': p.name,
      'nickname': p.nickname,
      'team': p.team,
      'role': p.role,
      'kills': p.kills,
      'assists': p.assists,
      'deaths': p.deaths,
      'totalGames': p.totalGames,
      'wins': p.wins,
    }
    return json.dumps(res)

  def delete(self,id):
    p = Player.query.get(id)
    db.session.delete(p)
    db.session.commit()
    res = {'id':id}
    return json.dumps(res)

  def put(self,id):
    p = Player.query.get(id)

    args = parser.parse_args()
    name = args['name']
    nickname = args['nickname']
    team = args['team']
    role = args['role']
    kills = args['kills']
    assists = args['assists']
    deaths = args['deaths']
    totalGames = args['totalGames']
    wins = args['wins']

    p.name = name
    p.nickname = nickname
    p.team = team
    p.role = role
    p.kills = kills
    p.assists = assists
    p.deaths = deaths
    p.totalGames = totalGames
    p.wins = wins
    db.session.commit()
    res = {}
    res[p.id] = {
      'name': p.name,
      'nickname': p.nickname,
      'team': p.team,
      'role': p.role,
      'kills': p.kills,
      'assists': p.assists,
      'deaths': p.deaths,
      'totalGames': p.totalGames,
      'wins': p.wins,
    }
    return json.dumps(res)

api.add_resource(
  PlayerAPI,
  '/api/player',
  '/api/player/<int:id>',
  '/api/player/<int:id>/<int:page>'
)
