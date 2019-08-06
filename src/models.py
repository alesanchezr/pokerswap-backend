from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Person {self.username}>'

    def serialize(self, admin=False):
        if admin:
            return {
                "id": self.id,
                "username": self.username,
                "email": self.email
            }
        return {
            "username": self.username
        }


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    players = db.Column(db.Integer)

    def __repr__(self):
        return f'<Tournament {self.name}>'

    def serialize(self, admin=False):
        if admin:
            return {
                "id": self.id,
                "name": self.name,
                "players": self.players
            }
        return {
            "username": self.username
        }