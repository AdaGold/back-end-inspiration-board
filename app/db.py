from flask_sqlalchemy import SQLAlchemy
print("Flask-SQLAlchemy is working!")
from flask_migrate import Migrate
from .models.base import Base


db = SQLAlchemy(model_class=Base)
migrate = Migrate()

