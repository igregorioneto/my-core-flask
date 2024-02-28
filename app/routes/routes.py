from flask import Blueprint

main_bp = Blueprint('main', __name__)

# Rota simples de acesso
@main_bp.route("/")
def index():
    return "Olá, mundo! Esta é minha primeira rota."

def configure_routes(app, use_auth=False):
    # Registrar rota principal
    app.register_blueprint(main_bp)

    # Verifica se a autenticação esta habilitada
    if use_auth:
        from .auth_routes import auth_bp
        app.register_blueprint(auth_bp)

