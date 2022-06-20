## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCCiFR0hqG5vZYLkTF9MDKeIdF93_DXZ2QsPOdftvOgRdy0nAeTAP6T1fc4JEVAPheCMOh_cx5-0GtHcxM-8sFbUXJBCSzIS3D1w39LDrKaYR3ghBuVb0aBG-3QHKnqo6XprTpHoUVz02sqhjXW8MOifpwXWC1lH9ZHAia7mO0oSnU8q0HrjuuZOqfPEkLVJ2sQD-Ed_Jju9O5xtqm89yme_xXMC-3aFa0blmGdglnQEbKfACAlA-Fz82sXtqjhDVWD2EEAnCFKtEEGUvNIEJiWhDIqxvttBsSiBKY7__kiEI2IYrRJy6nGs92gEwzZEAauuX69t6ssHWU0IVT7iWNCTB_hRgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5473789540:AAENvOyatn9WGFi6Odt7AcqyQKFBe6nusx0")
BOT_NAME = getenv("BOT_NAME", "ꫝꪗꨄ .")
API_ID = int(getenv("API_ID", "19303151"))
API_HASH = getenv("API_HASH", "69fcf6ca06865b043feef7d8948574f5")
OWNER_NAME = getenv("OWNER_NAME", "ꫝꪗ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "O_8_F")
ALIVE_NAME = getenv("ALIVE_NAME", "ꫝꪗ")
BOT_USERNAME = getenv("BOT_USERNAME", "AIIKM_BOT")
OWNER_ID = getenv("OWNER_ID", "1277157702")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "O_8_F")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AIIPM")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AIIPM")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
