from .base_model import BaseModel, db


class User(BaseModel):
    """Modelo para usuários"""

    __tablename__ = "tb_users"

    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
