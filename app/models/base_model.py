#from app import db

class BaseModel:
    """Classe base para todos os modelos."""
    __abstract__ = True

    def __init__(self, db):
        self.id = db.Column(db.Integer, primary_key=True)
        self.created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
        self.updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())