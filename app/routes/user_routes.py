from flask import Blueprint, jsonify
from app.models.user import User
from ..services import CRUDService

# Criando o blueprint referente ao User
def create_user_blueprint(db):
    user_bp = Blueprint('user', __name__)
    crud_service = CRUDService(db)

    @user_bp.route("/users", methods=['GET'])
    def get_all_users():
        users = crud_service.read_all(User(db=db))
        return jsonify(users)
    
    
    return user_bp
