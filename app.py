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

import os
from flask import Flask
from src.Utils.config import Config as cfg

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    port = int(cfg.FLASK_RUN_PORT)
    app.run(debug=True, port=port)
