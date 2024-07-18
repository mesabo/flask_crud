# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/15
🚀 Welcome to the Awesome Python Script 🚀

User: mesabo
Email: mesabo18@gmail.com / messouaboya17@gmail.com
Github: https://github.com/mesabo
Univ: Hosei University
Dept: Science and Engineering
Lab: Prof YU Keping's Lab
"""


from flask import Blueprint, request, jsonify, send_file
from ..Procedures.users_procedure import UserProcedure
from ..Utils.exceptions import UserValidationError, UserNotFoundError, UserDatabaseError
import os

users_bp_route = Blueprint('users', __name__)
user_procedure = UserProcedure()

@users_bp_route.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Flask CRUD app for Awesome Python Scripts'}), 200

@users_bp_route.route('/users/', methods=['GET'])
def get_users():
    try:
        users = user_procedure.get_all_users()
        return jsonify([user.dict() for user in users]), 200
    except UserDatabaseError as e:
        return jsonify({"error": str(e)}), 500

@users_bp_route.route('/users/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    try:
        user = user_procedure.get_user_by_id(user_id)
        return jsonify(user.dict()), 200
    except UserNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except UserDatabaseError as e:
        return jsonify({"error": str(e)}), 500

@users_bp_route.route('/users/', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        response = user_procedure.create_user(data)
        return jsonify({"message": response}), 201
    except UserValidationError as e:
        return jsonify({"error": str(e)}), 400
    except UserDatabaseError as e:
        return jsonify({"error": str(e)}), 500

@users_bp_route.route('/users/<int:user_id>/', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        response = user_procedure.update_user(user_id, data)
        return jsonify({"message": response}), 200
    except UserValidationError as e:
        return jsonify({"error": str(e)}), 400
    except UserNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except UserDatabaseError as e:
        return jsonify({"error": str(e)}), 500

@users_bp_route.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    try:
        response = user_procedure.delete_user(user_id)
        return jsonify({"message": response}), 200
    except UserNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except UserDatabaseError as e:
        return jsonify({"error": str(e)}), 500

@users_bp_route.route('/users/upload_csv', methods=['POST'])
def upload_csv():
    print("Yaya")

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        try:
            file_path = os.path.join('/tmp', file.filename)
            file.save(file_path)
            response = user_procedure.upload_csv(file_path)
            os.remove(file_path)  # Clean up the file after processing
            return jsonify({"message": response}), 201
        except UserValidationError as e:
            return jsonify({"error": str(e)}), 400
        except UserDatabaseError as e:
            return jsonify({"error": str(e)}), 500

@users_bp_route.route('/users/download_csv', methods=['GET'])
def download_csv():
    try:
        csv_data = user_procedure.download_csv()
        return send_file(
            csv_data,
            mimetype='text/csv',
            as_attachment=True,
            download_name='users.csv'
        )
    except UserDatabaseError as e:
        return jsonify({"error": str(e)}), 500
