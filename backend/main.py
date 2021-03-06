from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sse import sse
import flask_wtf
from application.config import Config
from application.database import db
from application.models import User, Role
from application.forms import ExtendedRegisterForm
from application import workers

from application.api import (
    UserAPI,
    UserDecksAPI,
    DeckAPI,
    DeckCardsAPI,
    CardAPI,
    DeckLastReviewTimeAPI,
    CardDifficultyAPI,
    DeckTotalScoreAPI,
    UserDataAPI,
    WebhookUrlAPI
)

from flask_security import Security, SQLAlchemySessionUserDatastore


app = None
api = None
celery = None


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    app.app_context().push()
    db.init_app(app)
    app.app_context().push()
    api = Api(app)
    app.app_context().push()
    db.create_all()
    app.app_context().push()
    user_datastore = SQLAlchemySessionUserDatastore(
        session=db.session, user_model=User, role_model=Role)
    app.app_context().push()
    security = Security(app, user_datastore,
                        register_form=ExtendedRegisterForm)
    app.app_context().push()
    # Create the celery instance
    celery = workers.celery
    app.app_context().push()
    
    # Update celery with the configuration
    celery.conf.update(
        broker_url = app.config["CELERY_BROKER_URL"],
        result_backend = app.config["CELERY_RESULT_BACKEND"],
        timezone = 'Asia/Kolkata',
        enable_utc = True
    )
    app.app_context().push()
    
    celery.Task = workers.ContextTask
    app.app_context().push()
    
    return app, api, celery


app, api, celery = create_app()
flask_wtf.CSRFProtect(app)

app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(sse, url_prefix='/stream')

CORS(app)

from application.controllers import *

api.add_resource(UserDataAPI, "/api/user_data/<int:user_id>")
api.add_resource(UserAPI, "/api/user/<int:user_id>")
api.add_resource(UserDecksAPI, "/api/deck/user/<int:user_id>")
api.add_resource(DeckAPI, "/api/deck", "/api/deck/<int:deck_id>")
api.add_resource(DeckCardsAPI, "/api/card/deck/<int:deck_id>")
api.add_resource(CardAPI, "/api/card", "/api/card/<int:card_id>")
api.add_resource(DeckLastReviewTimeAPI, "/api/deck/update_lrt/<int:deck_id>")
api.add_resource(CardDifficultyAPI,"/api/card/update_difficulty/<int:card_id>")
api.add_resource(DeckTotalScoreAPI,"/api/deck/update_ts/<int:deck_id>")
api.add_resource(WebhookUrlAPI,"/api/update_webhook_url/<int:user_id>")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port="5000"
    )
