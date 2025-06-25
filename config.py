from pathlib import Path

class Config(object):
    #basedir = os.path.abspath(os.path.dirname(__file__))
    basedir = Path(__file__).parent.absolute()

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
   # SQLALCHEMY_DATABASE_URI = r'sqlite:///' + os.path.join(Config.basedir, 'data.db').replace('\\', '/')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Config.basedir/"app.db"}'
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IP_HOST = 'localhost'
    PORT_HOST = 3000