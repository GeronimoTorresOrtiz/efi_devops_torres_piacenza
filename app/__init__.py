#Esta es la app principal que ejecuta flask
import os #

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') # el os enviroment trae desde ese entorno virtual lo que tiene la key del .env

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

load_dotenv() # Cargo la variable de entorno (.env) // trae todo lo que esta en el eentorno virtual a la aplicacion principal

from app.views import views #Estas son las vistas que flask va a ejecutar
