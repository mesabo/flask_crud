# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/14
🚀 Welcome to the Awesome Python Script 🚀

User: mesabo
Email: mesabo18@gmail.com / messouaboya17@gmail.com
Github: https://github.com/mesabo
Univ: Hosei University
Dept: Science and Engineering
Lab: Prof YU Keping's Lab
"""
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from src.Routes.users_route import users_bp_route
from src.Utils.exceptions import UserNotFoundError, UserValidationError, UserDatabaseError
from src.Utils.config import Config as cfg
import os
import json

app = Flask(__name__)
CORS(app)

# Load Swagger configuration from JSON file
with open('src/Data/swagger.json') as swagger_file:
    swagger_template = json.load(swagger_file)

swagger_template['host'] = cfg.SWAGGER_HOST
Swagger(app, template=swagger_template)

# Register the blueprint
app.register_blueprint(users_bp_route)


# Exception handling
@app.errorhandler(UserNotFoundError)
def handle_user_not_found_error(error):
    response = jsonify({"error": str(error)})
    response.status_code = 404
    return response


@app.errorhandler(UserValidationError)
def handle_user_validation_error(error):
    response = jsonify({"error": str(error)})
    response.status_code = 400
    return response


@app.errorhandler(UserDatabaseError)
def handle_user_database_error(error):
    response = jsonify({"error": str(error)})
    response.status_code = 500
    return response


@app.errorhandler(Exception)
def handle_generic_error(error):
    response = jsonify({"error": "An unexpected error occurred"})
    response.status_code = 500
    return response


if __name__ == '__main__':
    port = int(cfg.FLASK_RUN_PORT, 5000)
    app.run(debug=True, port=port)
