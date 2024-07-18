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

import pymysql
from ..Utils.config import Config as cfg

import pymysql
from pymysql.cursors import DictCursor
from ..Utils.config import Config as cfg


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host=cfg.DB_HOST,
            user=cfg.DB_USER,
            password=cfg.DB_PASSWORD,
            database=cfg.DB_NAME,
            cursorclass=DictCursor
        )

    def get_connection(self):
        return self.connection

