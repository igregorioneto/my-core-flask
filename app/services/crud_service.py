# Service genérico para ser instânciado
class CRUDService:
    def create(self, model_instance):
        from app import db
        self.db.session.add(model_instance)
        self.db.session.commit()

    def read_all(self, model_class):
        from app import db
        return model_class.query.all()
    
    def real_by_id(self, model_class, id):
        from app import db
        return model_class.query.get(id)
    
    def update(self, model_instance):
        from app import db
        self.db.session.commit()

    def delete(self, model_instance):
        from app import db
        self.db.session.delete(model_instance)
        self.db.session.commit()
    
