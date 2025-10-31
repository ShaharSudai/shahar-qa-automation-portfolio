from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
import argparse
from auth import auth_bp


app = Flask(__name__)
app.register_blueprint(auth_bp)

# JWT Config
app.config["JWT_SECRET_KEY"] = "a2f3c7e9-8b1d-4c55-a07f-41e5f938e612"
jwt = JWTManager(app)

# Swagger Config
swagger = Swagger(app, template={
    "info": {
        "title": "Bug Tracker API",
        "description": "QA Automation Portfolio – Bug Management API by Shahar Sudai",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Use: Bearer <your_token>"
        }
    }
})

from routes import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()
    app.run(debug=True, port=args.port)
