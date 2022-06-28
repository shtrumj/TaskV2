from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
#Migrate(app,db)
#login_manager =LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

