from sqlalchemy import and_
from flask_restful import (
    Resource,
    fields,
    marshal_with,
    reqparse,
    abort
)

from flask import request
from .database import db
from .models import User, Deck, Card
from .validations import APIError

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


user_fields = {
    "username" : fields.String,
    "email" : fields.String
}

deck_fields = {
    "deck_id": fields.Integer,
    "user_id": fields.Integer,
    "deck_name": fields.String,
    "last_review_time": fields.String,
    "total_score": fields.Integer
}

card_fields = {
    "card_id": fields.Integer,
    "deck_id": fields.Integer,
    "front": fields.String,
    "back": fields.String,
    "difficulty": fields.String
}


# Request Parsers
create_deck_parser = reqparse.RequestParser()
create_deck_parser.add_argument("user_id")
create_deck_parser.add_argument("deck_name")
create_deck_parser.add_argument("last_review_time")
create_deck_parser.add_argument("total_score")

update_deck_parser = reqparse.RequestParser()
update_deck_parser.add_argument("deck_name")
update_deck_parser.add_argument("last_review_time")
update_deck_parser.add_argument("total_score")

create_card_parser = reqparse.RequestParser()
create_card_parser.add_argument("deck_id")
create_card_parser.add_argument("front")
create_card_parser.add_argument("back")
create_card_parser.add_argument("difficulty")

update_card_parser = reqparse.RequestParser()
update_card_parser.add_argument("front")
update_card_parser.add_argument("back")
update_card_parser.add_argument("difficulty")


# Helper Functions
def abort_if_not_found(obj):
    if obj is None:
        abort(404, message="Resource not found")


def get_user(user_id):
    user = User.query.filter(User.id == user_id).scalar()
    return user


def validate_email(email):
    if (email is None) or (not re.fullmatch(regex, email)):
        raise APIError(
            status_code=400,
            error_code="USER_ERR_04",
            error_message="valid email is required"
        )


def validate_username(username):
    if (username is None) or (username.isnumeric()) or (len(username) == 0):
        raise APIError(
            status_code=400,
            error_code="USER_ERR_01",
            error_message="valid username is required"
        )


def validate_password(password):
    if (password is None) or (password.isnumeric()) or (len(password) == 0):
        raise APIError(
            status_code=400,
            error_code="USER_ERR_02",
            error_message="valid password is required"
        )


def get_deck(deck_id):
    deck = Deck.query.filter(Deck.deck_id == deck_id).scalar()
    return deck


def validate_deckname(deck_name):
    if (deck_name is None) or (deck_name.isnumeric()) or (len(deck_name) == 0):
        raise APIError(
            status_code=400,
            error_code="DECK_ERR_01",
            error_message="valid deck name is required"
        )


def validate_lastreviewtime(last_review_time):
    if last_review_time is None:
        return
    if (last_review_time.isnumeric()) or len(last_review_time) == 0:
        raise APIError(
            status_code=400,
            error_code="DECK_ERR_02",
            error_message="last review time should be either None or should be in valid datetime format"
        )


def validate_totalscore(total_score):
    if total_score is None:
        return
    if not total_score.isnumeric():
        raise APIError(
            status_code=400,
            error_code="DECK_ERR_03",
            error_message="total score should be either None or an integer"
        )


def get_card(card_id):
    card = Card.query.filter(Card.card_id == card_id).scalar()
    return card


def validate_front(front):
    if front is None or len(front) == 0:
        raise APIError(
            status_code=400,
            error_code="CARD_ERR_01",
            error_message="valid front is required"
        )


def validate_back(back):
    if back is None or len(back) == 0:
        raise APIError(
            status_code=400,
            error_code="CARD_ERR_02",
            error_message="valid back is required"
        )


def validate_difficulty(difficulty):
    if difficulty is None:
        return
    if difficulty not in ["easy", "medium", "hard"]:
        raise APIError(
            status_code=400,
            error_code="CARD_ERR_03",
            error_message="difficulty can only take the values null/Easy/Medium/Hard"
        )


# API Resources
class UserAPI(Resource):
    @marshal_with(user_fields)
    def get(self):
        auth_token = request.args['auth_token']
        if auth_token == 'secret':
            users = User.query.all()
            return users
        raise APIError(
            status_code=403,
            error_code="AUTH_ERR_01",
            error_message="invalid authentication token"
        )

    def delete(self, user_id):
        user = get_user(user_id)
        abort_if_not_found(user)
        db.session.delete(user)
        db.session.commit()
        return {"message" : "Successfully Deleted"}, 200

class UserDecksAPI(Resource):
    @marshal_with(deck_fields)
    def get(self, user_id):
        user = get_user(user_id)
        abort_if_not_found(user)
        decks = user.decks
        return decks


class DeckAPI(Resource):
    @marshal_with(deck_fields)
    def get(self, deck_id = None):
        deck = get_deck(deck_id)
        abort_if_not_found(deck)
        return deck

    @marshal_with(deck_fields)
    def put(self, deck_id):
        deck = get_deck(deck_id)
        abort_if_not_found(deck)
        args = update_deck_parser.parse_args()
        deck_name = args.get("deck_name", None)
        last_review_time = args.get("last_review_time", None)
        total_score = args.get("total_score", None)
        validate_deckname(deck_name)
        validate_lastreviewtime(last_review_time)
        validate_totalscore(total_score)
        deck.deck_name = deck_name
        deck.last_review_time = last_review_time
        deck.total_score = total_score
        db.session.commit()
        return deck

    def delete(self, deck_id):
        deck = get_deck(deck_id)
        abort_if_not_found(deck)
        db.session.delete(deck)
        db.session.commit()
        return {"message": "Successfully Deleted"}, 200

    @marshal_with(deck_fields)
    def post(self):
        args = create_deck_parser.parse_args()
        user_id = args.get("user_id", None)
        deck_name = args.get("deck_name", None)
        last_review_time = args.get("last_review_time", None)
        total_score = args.get("total_score", None)
        validate_deckname(deck_name)
        validate_lastreviewtime(last_review_time)
        validate_totalscore(total_score)
        user = get_user(user_id)
        if user is None:
            raise APIError(
                status_code=400,
                error_code="DECK_ERR_04",
                error_message="user does not exist"
            )
        deck = Deck.query.filter(and_(Deck.deck_name == deck_name, Deck.user_id == user_id)).scalar()
        if deck is not None:
            raise APIError(
                status_code=400,
                error_code="DECK_ERR_05",
                error_message="deck already exists"
            )
        deck = Deck(
            user_id=user_id,
            deck_name=deck_name,
            last_review_time=last_review_time,
            total_score=total_score
        )
        db.session.add(deck)
        db.session.commit()
        deck = Deck.query.filter(and_(Deck.deck_name == deck_name, Deck.user_id == user_id)).one()
        return deck, 201


class DeckCardsAPI(Resource):
    @marshal_with(card_fields)
    def get(self, deck_id):
        deck = get_deck(deck_id)
        abort_if_not_found(deck)
        cards = deck.cards
        return cards


class CardAPI(Resource):
    @marshal_with(card_fields)
    def get(self, card_id):
        card = get_card(card_id)
        abort_if_not_found(card)
        return card

    @marshal_with(card_fields)
    def put(self, card_id):
        card = get_card(card_id)
        abort_if_not_found(card)
        args = update_card_parser.parse_args()
        front = args.get("front", None)
        back = args.get("back", None)
        difficulty = args.get("difficulty", None)
        validate_front(front)
        validate_back(back)
        validate_difficulty(difficulty)
        card.front = front
        card.back = back
        card.difficulty = difficulty
        db.session.commit()
        return card

    def delete(self, card_id):
        card = get_card(card_id)
        abort_if_not_found(card)
        db.session.delete(card)
        db.session.commit()
        return {"message": "Successfully Deleted"}, 200

    @marshal_with(card_fields)
    def post(self):
        args = create_card_parser.parse_args()
        deck_id = args.get("deck_id", None)
        front = args.get("front", None)
        back = args.get("back", None)
        difficulty = args.get("difficulty", None)
        validate_front(front)
        validate_back(back)
        validate_difficulty(difficulty)
        deck = get_deck(deck_id)
        if deck is None:
            raise APIError(
                status_code=400,
                error_code="CARD_ERR_04",
                error_message="deck does not exist"
            )
        card = Card(
            deck_id=deck_id,
            front=front,
            back=back,
            difficulty=difficulty
        )
        db.session.add(card)
        db.session.commit()
        return card, 201

class DeckLastReviewTimeAPI(Resource):
    @marshal_with(deck_fields)
    def put(self,deck_id):
        deck = get_deck(deck_id)
        abort_if_not_found(deck)
        args = update_deck_parser.parse_args()
        last_review_time = args.get("last_review_time", None)
        validate_lastreviewtime(last_review_time)
        deck.last_review_time = last_review_time
        db.session.commit()
        return deck

class CardDifficultyAPI(Resource):
    @marshal_with(card_fields)
    def put(self,card_id):
        card = get_card(card_id)
        abort_if_not_found(card)
        args = update_card_parser.parse_args()
        difficulty = args.get("difficulty", None)
        validate_difficulty(difficulty)
        card.difficulty = difficulty
        db.session.commit()
        return card

class DeckTotalScoreAPI(Resource):
    @marshal_with(deck_fields)
    def put(self,deck_id):
        deck = get_deck(deck_id)
        abort_if_not_found(deck)
        args = update_deck_parser.parse_args()
        total_score = args.get("total_score", None)
        validate_totalscore(total_score)
        deck.total_score = total_score
        db.session.commit()
        return deck