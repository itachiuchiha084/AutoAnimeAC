import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env')
elif os.path.exists("sample.env"):
    load_dotenv("sample.env")

API_ID = os.getenv("API_ID","27108998")
API_HASH = os.getenv("API_HASH","f4fc03493766db361d7e85ed8974fe2f")
BOT_TOKEN = os.getenv("BOT_TOKEN","5989024511:AAGQuNKayfE0n--SV5o4ONgyWdQKVpQDZaI")
MONGO_DB_URI = os.getenv("MONGO_DB_URI","mongodb+srv://naruto:naruto@cluster0.h9wsftd.mongodb.net/?retryWrites=true&w=majority")
STATUS_MSG_ID = os.getenv("STATUS_MSG_ID","Anime_Alliance/3")
SCHEDULE_MSG_ID = os.getenv("SCHEDULE_MSG_ID","anime_ongoing_uploadsC/2")
CHANNEL_TITLE = os.getenv("CHANNEL_TITLE", "Anime_Alliance")
INDEX_CHANNEL_USERNAME = os.getenv("INDEX_CHANNEL_USERNAME","Anime_Alliance")
UPLOADS_CHANNEL_USERNAME = os.getenv("UPLOADS_CHANNEL_USERNAME","anime_ongoing_uploads")
TECHZ_API_KEY = os.getenv("TECHZ_API_KEY","EQRQFH")
COMMENTS_GROUP_LINK = os.getenv("COMMENTS_GROUP_LINK", "https://t.me/+5-_jTUAhGTpiY2Vl")
SLEEP_TIME = os.getenv("SLEEP_TIME", 60)

for k, v in {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "MONGO_DB_URI": MONGO_DB_URI,
    "STATUS_MSG_ID": STATUS_MSG_ID,
    "SCHEDULE_MSG_ID": SCHEDULE_MSG_ID,
    "INDEX_CHANNEL_USERNAME": INDEX_CHANNEL_USERNAME,
    "UPLOADS_CHANNEL_USERNAME": UPLOADS_CHANNEL_USERNAME,
    "TECHZ_API_KEY": TECHZ_API_KEY,
    "COMMENTS_GROUP_LINK": COMMENTS_GROUP_LINK,
}.items():
    if not v:
        raise Exception(f"{k} not found .env file, please add it to use AutoAnimeBot")
