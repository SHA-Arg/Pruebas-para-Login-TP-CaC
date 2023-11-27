class Config:
    SECRET_KEY = '!@#Secret'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask_login'


config = {
    'development': DevelopmentConfig
}
