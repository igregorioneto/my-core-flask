from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .routes.routes import configure_routes


db = SQLAlchemy()
migrate = Migrate()
# Função principal
def create_app(use_auth=False, use_db=False, db_uri=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registro do Blueprint
    # app.register_blueprint(main_bp)    

    if use_db:
        if db_uri:
            app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.__init__(app)
    migrate.__init__(app, db)

    configure_routes(app=app, use_auth=use_auth, db=db)

    return app