from flask import Blueprint

# Blueprint para rotas de autenticação
auth_bp = Blueprint('auth', __name__)

# Rota de login
@auth_bp.route("/login")
def login():
    return 'Página de login'

# Rota de logout
@auth_bp.route("/logout")
def logout():
    return 'Página de logout'
