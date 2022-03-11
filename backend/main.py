from flask import Flask
from flask_restful import Api
from application.config import Config
from application.database import db
from application.models import User, Role
from application.forms import ExtendedRegisterForm

from application.api import (
    UserAPI,
    UserDecksAPI,
    DeckAPI,
    DeckCardsAPI,
    CardAPI,
    DeckLastReviewTimeAPI,
    CardDifficultyAPI,
    DeckTotalScoreAPI
)

from flask_security import Security, SQLAlchemySessionUserDatastore


app = None
api = None


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    user_datastore = SQLAlchemySessionUserDatastore(
        session=db.session, user_model=User, role_model=Role)
    security = Security(app, user_datastore,
                        register_form=ExtendedRegisterForm)
    return (app, api, security, user_datastore)


app, api, security, user_datastore = create_app()

from application.controllers import *

api.add_resource(UserAPI, "/api/user", "/api/user/<int:user_id>")
api.add_resource(UserDecksAPI, "/api/deck/user/<int:user_id>")
api.add_resource(DeckAPI, "/api/deck", "/api/deck/<int:deck_id>")
api.add_resource(DeckCardsAPI, "/api/card/deck/<int:deck_id>")
api.add_resource(CardAPI, "/api/card", "/api/card/<int:card_id>")
api.add_resource(DeckLastReviewTimeAPI, "/api/deck/update_lrt/<int:deck_id>")
api.add_resource(CardDifficultyAPI,"/api/card/update_difficulty/<int:card_id>")
api.add_resource(DeckTotalScoreAPI,"/api/deck/update_ts/<int:deck_id>")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port="5000"
    )
