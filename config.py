import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", "8658860"))

    API_HASH = os.environ.get("API_HASH", "fbb92e01e221f45920e63eb7000e4e38")
    
    API_KEY = os.environ.get("API_KEY", "")

    
