class Config:
    """Configurações base do aplicativo Flask"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Configurações para o ambiente de desenvolvimento"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurações para o ambiente de produção"""
    SECRET_KEY = 'chave_secreta_personalizada_para_producao'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site_prod.db'

class TestingConfig(Config):
    """Configuração para o ambiente de teste"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'