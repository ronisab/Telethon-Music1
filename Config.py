import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "2156559"))
    API_HASH = os.environ.get("API_HASH", "fea80bd8ede83bcb1a3290c43e5691bd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2138748531:AAHfB17Vd1KZVsUqhblKcIQuHMH9NQRWVbU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBuw4qTOfxeMXfuU6JbbX-PBuLMQchOJLefm82xroi-KwsCLB59-VLO3I_1wtRrbF5g05WgwTsC4yXj0xgBv-1xEG-NEkFY9ciBMaflMbDRwUS9aFJqeVlbKT752RXAw-zkf4cSUfxi8qISDPdQmoWcEJlYpcHBZdxXG18ADuIkVaVUAoIWKAQx0x7funPiSdK_rNc9nphFoJnZZKaky-dt9SEQkHpPXx7RJUJN9ElCgn0Nz0lakVfSo9iiWfM6A4SrnmQwtQNnm5NIVmnh1iQaHY_kDjtC8Qx1Q_mplAP_T1aImtbVkVnK9rYU8aatf0bovQ3GTuZKDOTwZd_B189WuA=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "kylieverzosabot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1492235056"))
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
