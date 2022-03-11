from .database import db
from flask_security import UserMixin, RoleMixin

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer, db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    active = db.Column(db.Boolean)
    roles = db.relationship('Role', secondary = roles_users, backref = db.backref('user', lazy = 'dynamic'))
    decks = db.relationship('Deck', backref = 'user', cascade = "all, delete")

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    description = db.Column(db.String)

class Deck(db.Model):
    __tablename__ = 'deck'
    deck_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    deck_name = db.Column(db.String, unique = True, nullable = False)
    last_review_time = db.Column(db.String)
    total_score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    cards = db.relationship('Card', backref = 'deck', cascade = "all, delete")

class Card(db.Model):
    __tablename__ = 'card'
    card_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    deck_id = db.Column(db.Integer, db.ForeignKey("deck.deck_id"), nullable = False)
    front = db.Column(db.String, nullable = False)
    back = db.Column(db.String, nullable = False)
    difficulty = db.Column(db.String)  