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


class UserException(Exception):
    """Base exception class for all User related exceptions"""
    pass

class UserNotFoundError(UserException):
    """Exception raised when a User item is not found"""
    def __init__(self, message="User item not found"):
        self.message = message
        super().__init__(self.message)

class UserValidationError(UserException):
    """Exception raised for validation errors"""
    def __init__(self, message="Validation error"):
        self.message = message
        super().__init__(self.message)

class UserDatabaseError(UserException):
    """Exception raised for database operation errors"""
    def __init__(self, message="Database operation error"):
        self.message = message
        super().__init__(self.message)

