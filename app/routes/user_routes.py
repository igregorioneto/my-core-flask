from flask import Blueprint, jsonify, request
from app.models.user import User
from app.services import CRUDService
from app import db

user_bp = Blueprint('user', __name__)
crud_service = CRUDService(db)

@user_bp.route("/users", methods=['GET'])
def get_all_users():
    users = crud_service.read_all(User)
    return jsonify(users)
