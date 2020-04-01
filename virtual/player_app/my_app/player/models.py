from my_app import db

class Player(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  nickname = db.Column(db.String(255))
  team = db.Column(db.String(255))
  role = db.Column(db.String(255))
  kills = db.Column(db.Integer)
  assists = db.Column(db.Integer)
  deaths = db.Column(db.Integer)
  totalGames = db.Column(db.Integer)
  wins = db.Column(db.Integer)

  def __init__(self,name,nickname,team,role,kills,assists,deaths,totalGames,wins):
    self.name = name
    self.nickname = nickname
    self.team = team
    self.role = role
    self.kills = kills
    self.assists = assists
    self.deaths = deaths
    self.totalGames = totalGames
    self.wins = wins

  def __repr_(self):
    return 'Player {0}'.format(self.id)

