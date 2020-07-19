from util.Util import get_variable

class Config:
    # Configuration Instructions
    SECRET_KEY = get_variable('SECRET_KEY')
    MAIL_SERVER = get_variable('MAIL_SERVER'. 'smtp.google.com')
    MAIL_PORT = get_variable('MAIL_PORT', 587)
    MAIL_USE_TLS = get_variable('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = get_variable('MAIL_USERNAME')
    MAIL_PASSWORD = get_variable('MAIL_PASSOWRD')
    MIND_MAIL_SUBJECT_PREFIX = 'Mind'
    MIND_MAIL_SENDER = 'Mind <noreply@mind.com>'
    MIND_ADMIN = get_variable('MIND_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_variable('DEV_DATABASE_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = get_variable('TEST_DATABASE_URL')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_variable('DATABASE_URL')

config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
