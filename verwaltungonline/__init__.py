from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_oauthlib.client import OAuth2Client
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISSECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['OAUTH2_CLIENT_ID'] = 'verwaltung.wp472.de'
app.config['OAUTH2_CLIENT_SECRET'] = 'your-client-secret'
app.config['OAUTH2_SERVER_METADATA_URL'] = 'https://login.wp472.de/realms/wp472.de/.well-known/openid-configuration'
app.config['OAUTH2_CLIENT_KWARGS'] = {'scope': 'openid email profile'}

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
oauth_provider = OAuth2Provider(app)

from verwaltungonline import routes
