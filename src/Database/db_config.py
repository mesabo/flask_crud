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

from pymongo import MongoClient
from ..Utils.config import Config as cfg


class Database:
    def __init__(self):
        self.client = MongoClient(cfg.MONGO_URL)
        self.db = self.client[cfg.DB_NAME]

    def get_db(self):
        return self.db
