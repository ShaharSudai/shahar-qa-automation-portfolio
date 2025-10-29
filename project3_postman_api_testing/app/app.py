from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
import argparse
from auth import auth_bp


app = Flask(__name__)
app.register_blueprint(auth_bp)

# JWT Config
app.config["JWT_SECRET_KEY"] = "secret-change-this"
jwt = JWTManager(app)

# Swagger Config
swagger = Swagger(app, template={
    "info": {
        "title": "Bug Tracker API",
        "description": "Simple Bug Tracking API with Auth, Status Flow and Comments",
        "version": "1.0"
    }
})

from routes import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()
    app.run(debug=True, port=args.port)
