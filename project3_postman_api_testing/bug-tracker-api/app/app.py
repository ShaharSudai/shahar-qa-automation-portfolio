from flask import Flask
from flasgger import Swagger
import argparse


app = Flask(__name__)


# Swagger Config
swagger = Swagger(app, template={
    "info": {
        "title": "Bug Tracker API",
        "description": "QA Automation Portfolio – Bug Management API by Shahar Sudai",
        "version": "1.0.0"
    }
})

from routes import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()
    app.run(debug=True, port=args.port)
