from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID", "23842900")
API_HASH = getenv("API_HASH", "d21e95895cf2a5b83b0167fdd3b6e541")

BOT_TOKEN = getenv("BOT_TOKEN", "5915949693:AAGkojAqOwW5W7RFnJ2OzRDu5c4LqjtpRII")
LOGGER_ID = int(getenv("LOGGER_ID", "-1001126273421"))
OWNER_ID = int(getenv("OWNER_ID", "5761513990"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Xx:Xx@cluster0.mwyxrf1.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "ariyan_server")
