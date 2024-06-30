import os

class Config:
    SECRET_KEY : str
    SQLALCHEMY_DATABASE_URI : str

class DefaultConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///default.db')

class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'