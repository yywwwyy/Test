# encoding=utf-8
"""
@Description :
@Project ：behavior-recognition
@File    ：util.py
@Author  ：
@Date    ：
"""

import json
import time
import datetime


def load_config():
    with open("./config.json", mode="r", encoding="utf-8") as f:
        res = json.load(f)

    return res
