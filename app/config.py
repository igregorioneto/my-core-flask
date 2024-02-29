from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """Configurações base do aplicativo Flask"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "key"
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
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