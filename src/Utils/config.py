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

import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()


class Config:
    MONGO_URL = os.getenv("MONGO_URL")
    DB_URL = os.getenv("DB_URL")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", 5000)
    SWAGGER_HOST = os.getenv("SWAGGER_HOST", "localhost:5000")

    # Use relative path to load the config.json
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)
    data_dir = os.path.join(project_root, 'Data')
    config_path = os.path.join(data_dir, 'tables.json')

    with open(config_path) as f:
        config = json.load(f)

    COL_USERS = config.get('collections', {}).get('users_col', 'Users')

    def test_data(self) -> json:
        test_data_path = os.path.join(self.data_dir, 'test_data.json')

        with open(test_data_path) as f:
            return json.load(f)
