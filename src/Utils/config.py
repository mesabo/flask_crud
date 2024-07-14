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

# Utils/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    MONGO_URL = os.getenv("MONGO_URL")
    DB_URL = os.getenv("DB_URL")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", 5000)