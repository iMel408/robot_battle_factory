from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.now())
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        """Show info about user"""
        return f"<User user_id={self.user_id} email={self.email}>"


class Battle(db.Model):

    __tablename__= 'battles'

    battle_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(256), nullable=False)
    team_size = db.Column(db.Integer, nullable=False, default=5)
    is_active = db.Column(Boolean, unique=False, default=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.now())
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.now())


    def __repr__(self):
        """Show info about robots"""
        return f"<Battle id={self.battle_id} title={self.title}>"



class Robot(db.Model):

    __tablename__ = 'robots'

    unit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.battle_id'))
    name = db.Column(db.String(64), nullable=False)
    team = db.Column(db.String(16), nullable=False)
    is_active = db.Column(Boolean, unique=False, default=True)
    health_lvl = db.Column(db.Integer, nullable=False, default=100)
    charge_lvl = db.Column(db.Integer, nullable=False, default=100)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.now())
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.now())


    def __repr__(self):
        """Show info about robots"""
        return f"<Robot unit_id={self.rating_id} battle_id={self.battle_id} user_id={self.user_id}>"

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///botwars'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from app import app
    connect_to_db(app)
    print("Connected to DB.")