# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL=f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PWD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}"
class Config:
    ''' Base config class'''
    DEBUG = False

class DevelopmentConfig(Config):
    ''' Configuration for dev'''
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    DEBUG = True

class TestingConfig(Config):
    ''' Configuration for test'''
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration mapping
config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig
}