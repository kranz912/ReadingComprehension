import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "63C9BD48A2C1ECBD8679D1657944A"
