from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configure your app
    app.config['SECRET_KEY'] = '438589742fdf4cbd9a6a40b22778927c'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dennis:password123@localhost:5432/tiresreview'

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User, Article

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    return app
