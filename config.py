# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "18442173")

API_HASH = os.environ.get("API_HASH", "115d8326136c0fe629f02082500a044d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7192362340:AAE7nXufgNpYHBOreGwwkiQowRl7vJ7y4xs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "PixelPartyUpdates") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamer")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://pprenamer:pprenamer@cluster0.unnx5eg.mongodb.net/")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
