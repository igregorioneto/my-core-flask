from .base_model import BaseModel

class User(BaseModel):
    """Modelo para usuários"""

    __tablename__ = "tb_users"

    def __init__(self, db):
        super().__init__(db)  # Chame o construtor de BaseModel

        self.username = db.Column(db.String(50), unique=True, nullable=False)
        self.email = db.Column(db.String(120), unique=True, nullable=False)
        self.password = db.Column(db.String(255), nullable=False)
