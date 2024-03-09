from flask import Blueprint
from .user_routes import create_user_blueprint

main_bp = Blueprint('main', __name__)

# Rota simples de acesso
@main_bp.route("/")
def index():
    return "Olá, mundo! Esta é minha primeira rota."

# Configuração das rotas
def configure_routes(app, use_auth=False, db=None):
    # Criando o blueprint
    user_bp = create_user_blueprint()
    
    #Registrando Rotas
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    # Verifica se a autenticação esta habilitada
    if use_auth:
        from .auth_routes import auth_bp
        app.register_blueprint(auth_bp)

