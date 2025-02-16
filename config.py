#Coded by KA18 the @legend580 💛❤️

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class tuple_(object):
    def __init__(self):
        return

class Config(object):

    #BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6100891233:AAEPZ22I2sI3IPVWDcsAC1X3Ydf1XqM6qvA") #testing bot 1 (ghfjg)
    #BOT_TOKEN = os.environ.get("BOT_TOKEN", "6100891233:AAEPZ22I2sI3IPVWDcsAC1X3Ydf1XqM6qvA") #testing bot 2 (url_v3)
    
    API_ID = int(os.environ.get("API_ID", ""))

    API_HASH = os.environ.get("API_HASH", "")

    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    AUTH_USERS = list(AUTH_USERS)
    
    AUTH_USERS.append(OWNER_ID)
    
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    #DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))

    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    DATABASE_NAME = os.environ.get("DATABASE_NAME", "")
    
    LOGGER = logging
    
    #Port
    PORT = os.environ.get("PORT", "8080")
