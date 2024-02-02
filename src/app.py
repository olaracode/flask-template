from flask import Flask
from flask_migrate import Migrate
from .User.routes import user as UserRouter # -> Importo el router de el modulo USER
import os
from .db import db



app = Flask(__name__)

DB_URL = os.environ.get("POSTGRES_URL")

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL

MIGRATE = Migrate(app, db)

# Initializamos la base de datos
db.init_app(app)

app.register_blueprint(UserRouter, url_prefix="/usuario")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)