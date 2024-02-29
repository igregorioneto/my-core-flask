class CRUDService:
    def __init__(self, db):
        self.db = db

    def create(self, model_instance):
        self.db.session.add(model_instance)
        self.db.session.commit()

    def read_all(self, model_class):
        return model_class.query.all()
    
    def real_by_id(self, model_class, id):
        return model_class.query.get(id)
    
    def update(self, model_instance):
        self.db.session.commit()

    def delete(self, model_instance):
        self.db.session.delete(model_instance)
        self.db.session.commit()
    
