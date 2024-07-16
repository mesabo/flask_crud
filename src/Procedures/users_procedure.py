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

from datetime import datetime
from io import BytesIO
from typing import Dict, Any, List
import pandas as pd
from ..Models.users_model import UsersModel
from ..Services.users_service import UsersService
from ..Utils.exceptions import UserDatabaseError, UserValidationError, UserNotFoundError
from ..Utils.config import Config as cfg

class UserProcedure:
    def __init__(self):
        self.users_service = UsersService()
        self.users_collection = cfg.COL_USERS

    def get_user_by_username_or_email_or_phone(self, username: str, email: str, phone: str) -> UsersModel:
        criteria = {"$or": [{"username": username}, {"email": email}, {"phone": phone}]}
        try:
            user = self.users_service.find(criteria, self.users_collection)
            if not user:
                raise UserNotFoundError(f"User with username {username}, email {email}, phone {phone} not found")
            return UsersModel.from_mongo(user[0])
        except Exception as e:
            raise UserDatabaseError(f"Error finding user: {str(e)}")

    def get_user_by_id(self, user_id: str) -> UsersModel:
        try:
            user = self.users_service.findById(user_id, self.users_collection)
            if not user:
                raise UserNotFoundError(f"User with id {user_id} not found")
            return UsersModel.from_mongo(user)
        except Exception as e:
            raise UserDatabaseError(f"Error finding user by id: {e}")

    def get_all_users(self) -> List[UsersModel]:
        try:
            users = self.users_service.find({}, self.users_collection)
            users_list = [UsersModel.from_mongo(user) for user in users]
            return users_list
        except Exception as e:
            raise UserDatabaseError(f'Error finding all users: {str(e)}')

    def create_user(self, user_data: Dict[str, Any]) -> str:
        try:
            user = UsersModel(**user_data)
            user.created_at = datetime.now()
            user.updated_at = datetime.now()
            created = self.users_service.insertOne(user, self.users_collection)
            return f'Inserted userId {created}'
        except Exception as e:
            raise UserDatabaseError(f"Error inserting user: {str(e)}")

    def create_users(self, users_data: List[Dict[str, Any]]) -> List[str]:
        try:
            users = [UsersModel(**user_data) for user_data in users_data]
            for user in users:
                user.created_at = datetime.now()
                user.updated_at = datetime.now()
            created_ids = self.users_service.insertMany(users, self.users_collection)
            return created_ids
        except Exception as e:
            raise UserDatabaseError(f"Error inserting users: {str(e)}")

    def update_user(self, user_id: str, update_data: Dict[str, Any]) -> str:
        try:
            user = UsersModel(**update_data)
            user.updated_at = datetime.now()
            updated = self.users_service.update(user_id, user, self.users_collection)
            return updated
        except Exception as e:
            raise UserDatabaseError(f"Error updating user: {str(e)}")

    def delete_user(self, user_id: str) -> str:
        try:
            deleted = self.users_service.deleteOne(user_id, self.users_collection)
            return deleted
        except Exception as e:
            raise UserDatabaseError(f"Error deleting user: {str(e)}")

    def delete_users(self, user_ids: List[str]) -> List[str]:
        try:
            deleted = self.users_service.deleteMany(user_ids, self.users_collection)
            return deleted
        except Exception as e:
            raise UserDatabaseError(f"Error deleting users: {str(e)}")

    def download_csv(self) -> BytesIO:
        try:
            users = self.get_all_users()
            df = pd.DataFrame([user.dict() for user in users])
            output = BytesIO()
            df.to_csv(output, index=False)
            output.seek(0)
            return output
        except Exception as e:
            raise UserDatabaseError(f"Error downloading CSV: {str(e)}")

    def upload_csv(self, file_path: str) -> str:
        try:
            data = pd.read_csv(file_path)
            users_data = []
            for index, row in data.iterrows():
                user_data = {
                    "username": row["username"],
                    "fullname": row["fullname"],
                    "email": row["email"],
                    "phone": row["phone"],
                    "address": {
                        "street": row["address.street"],
                        "city": row["address.city"],
                        "state": row["address.state"],
                        "zipcode": row["address.zipcode"],
                        "country": row["address.country"]
                    },
                    "is_active": row["is_active"],
                    "created_at": datetime.strptime(row["created_at"], "%Y-%m-%d %H:%M:%S"),
                    "updated_at": datetime.strptime(row["updated_at"], "%Y-%m-%d %H:%M:%S")
                }
                users_data.append(user_data)
            self.create_users(users_data)
            return "CSV content uploaded and saved successfully"
        except KeyError as e:
            raise UserValidationError(f"Missing required field in CSV: {str(e)}")
        except Exception as e:
            raise UserDatabaseError(f"Error uploading CSV: {str(e)}")
