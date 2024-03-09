from flask import Blueprint, jsonify
from app.models.user import User
from ..services import CRUDService

# Criando o blueprint referente ao User
def create_user_blueprint():
    user_bp = Blueprint('user', __name__)
    crud_service = CRUDService()

    @user_bp.route("/users", methods=['GET'])
    def get_all_users():
        from app import db
        users = crud_service.read_all(User)
        return jsonify(users)
    
    
    return user_bp
