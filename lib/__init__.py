import os

class config :
    API_ID = os.environ.get("API_ID","")
    API_HASH = os.environ.get("API_HASH","")
    TOKEN = os.environ.get("TOKEN","")
    SESSION = os.environ.get("SESSION","")
    CLIENT_ID = os.environ.get("CLIENT_ID","")
    SECRET = os.environ.get("SECRET","")
