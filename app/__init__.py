from flask import Flask, Blueprint
from .config import Config

# Criando um blueprint para as rotas
main_bp = Blueprint('main', __name__)

# Rota simples de acesso
@main_bp.route("/")
def index():
    return "Olá, mundo! Esta é minha primeira rota."

# Função principal
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registro do Blueprint
    app.register_blueprint(main_bp)

    return app