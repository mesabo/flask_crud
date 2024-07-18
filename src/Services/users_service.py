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
from typing import List, Dict, Any
from ..Database.db_config import Database
from ..Models.users_model import UsersModel, Address


class UsersService:
    def __init__(self):
        db_manager = Database()
        self.connection = db_manager.get_connection()

    def insert_one(self, element: UsersModel) -> int:
        with self.connection.cursor() as cursor:
            sql_user = """
                INSERT INTO Users (username, fullname, email, phone, is_active, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_user, (
                element.username, element.fullname, element.email,
                element.phone, element.is_active, element.created_at, element.updated_at
            ))
            user_id = cursor.lastrowid

            sql_address = """
                INSERT INTO Address (street, city, state, zipcode, country, user_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_address, (
                element.address.street, element.address.city, element.address.state,
                element.address.zipcode, element.address.country, user_id
            ))

        self.connection.commit()
        return user_id

    def insert_many(self, elements: List[UsersModel]) -> List[int]:
        user_ids = []
        with self.connection.cursor() as cursor:
            for element in elements:
                user_id = self.insert_one(element)
                user_ids.append(user_id)
        return user_ids

    def find(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM Users"
            cursor.execute(sql)
            users = cursor.fetchall()

            sql = "SELECT * FROM Address WHERE user_id = %s"
            for user in users:
                cursor.execute(sql, (user['id'],))
                address = cursor.fetchone()
                user['address'] = address

        return users

    def find_by_id(self, id: int) -> Dict[str, Any]:
        with self.connection.cursor() as cursor:
            sql_user = "SELECT * FROM Users WHERE id = %s"
            cursor.execute(sql_user, (id,))
            user = cursor.fetchone()

            if user:
                sql_address = "SELECT * FROM Address WHERE user_id = %s"
                cursor.execute(sql_address, (id,))
                address = cursor.fetchone()
                user['address'] = address

        return user

    def update(self, id: int, element: UsersModel) -> str:
        with self.connection.cursor() as cursor:
            sql_user = """
                UPDATE Users SET username = %s, fullname = %s, email = %s, phone = %s, is_active = %s, updated_at = %s
                WHERE id = %s
            """
            cursor.execute(sql_user, (
                element.username, element.fullname, element.email,
                element.phone, element.is_active, element.updated_at, id
            ))

            sql_address = """
                UPDATE Address SET street = %s, city = %s, state = %s, zipcode = %s, country = %s
                WHERE user_id = %s
            """
            cursor.execute(sql_address, (
                element.address.street, element.address.city, element.address.state,
                element.address.zipcode, element.address.country, id
            ))

        self.connection.commit()
        return "Record updated successfully"

    def delete_one(self, id: int) -> str:
        with self.connection.cursor() as cursor:
            sql_user = "DELETE FROM Users WHERE id = %s"
            cursor.execute(sql_user, (id,))

        self.connection.commit()
        return "Record deleted successfully"
