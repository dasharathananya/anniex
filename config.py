import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials - Get these from the Telegram API website
API_ID = int(getenv("29844041"))
API_HASH = getenv("afe565347828546c67d9a3fdb94a4fae")
BOT_TOKEN = getenv("7448446414:AAERt1dhE1YngpQIvZ0Pxh0NLfhKldNTA-Y")

# Specify where to get the following credentials
OWNER_USERNAME = getenv("@KALI_LINUX_NET", "MrBrokn")
BOT_USERNAME = getenv("@Ananya_musicbot", "MISS_YUMIPRO_BOT")
BOT_NAME = getenv("BOT_NAME", "‣ 𝘼𝙉𝙉𝘼𝙔𝘼 𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏 ")
ASSUSERNAME = getenv("@ANANYA_MUSIC_ASSISTANT", "🎧 𝘼𝙉𝘼𝙉𝙔𝘼 ✘ 𝙈𝙐𝙎𝙄𝘾 ➛")
EVALOP = list(map(int, getenv("EVALOP", "1841914911").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("-1002245560052", -1002094142057))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# External APIs - Get these from their respective providers
GPT_API = getenv("https://api.openai.com/v1/organization/projects/{project_id}/api_keys")
DEEP_API = getenv("DEEP_API")
OWNER_ID = int(getenv("7068157354", 7068157354))

# Heroku deployment settings - Refer to Heroku documentation on how to obtain these
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/MRXBROKEN011/anniex")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support and contact information - Provide your own support channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Ananya_x_music")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", ""https://t.me/WEST_BENGAL_HACKR)

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Server limits and configurations - These can be set based on your server configurations
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# External service credentials - Obtain these from Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# Telegram file size limits - Set these according to your requirements
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Pyrogram session strings - You need to generate these yourself
STRING1 = getenv("BQHHYkkAuz2l7z7APDam5Q02nLKDHxA6xH_ieN9ReqV3S2tu_Ak2tuviD1I88eec4w1eE2GFHOrdDS9wNfakWXJtuEEA1hqJsulZ9KsDPZRKuuV2wnvnJUKYYM_RKcN0iu52Z36boXn4_pOt8p6ejM9vKtFrEX1Knz8Sh46O4IVurcIdj4wJUS6avmRYYHjNOFl0O4dOlGiVmvsKq_vkvhFrcpXqiFgt9-OYk1mtz5YCuaTpl0wFmcmW11qUxfhOit9RqBSW2c3FkrjI9NWRivuc9HutcF2_wSFRapSViOlJz9262I7vQchKG9VURgdfXVfmQY1tE4R5iF4aT-ruY6cQf0-j6QAAAAGFpL8IAA", None)
STRING2 = getenv("BQHHYkkAuz2l7z7APDam5Q02nLKDHxA6xH_ieN9ReqV3S2tu_Ak2tuviD1I88eec4w1eE2GFHOrdDS9wNfakWXJtuEEA1hqJsulZ9KsDPZRKuuV2wnvnJUKYYM_RKcN0iu52Z36boXn4_pOt8p6ejM9vKtFrEX1Knz8Sh46O4IVurcIdj4wJUS6avmRYYHjNOFl0O4dOlGiVmvsKq_vkvhFrcpXqiFgt9-OYk1mtz5YCuaTpl0wFmcmW11qUxfhOit9RqBSW2c3FkrjI9NWRivuc9HutcF2_wSFRapSViOlJz9262I7vQchKG9VURgdfXVfmQY1tE4R5iF4aT-ruY6cQf0-j6QAAAAGFpL8IAA", None)
STRING3 = getenv("BQHHYkkAuz2l7z7APDam5Q02nLKDHxA6xH_ieN9ReqV3S2tu_Ak2tuviD1I88eec4w1eE2GFHOrdDS9wNfakWXJtuEEA1hqJsulZ9KsDPZRKuuV2wnvnJUKYYM_RKcN0iu52Z36boXn4_pOt8p6ejM9vKtFrEX1Knz8Sh46O4IVurcIdj4wJUS6avmRYYHjNOFl0O4dOlGiVmvsKq_vkvhFrcpXqiFgt9-OYk1mtz5YCuaTpl0wFmcmW11qUxfhOit9RqBSW2c3FkrjI9NWRivuc9HutcF2_wSFRapSViOlJz9262I7vQchKG9VURgdfXVfmQY1tE4R5iF4aT-ruY6cQf0-j6QAAAAGFpL8IAA", None)
STRING4 = getenv("BQHHYkkAuz2l7z7APDam5Q02nLKDHxA6xH_ieN9ReqV3S2tu_Ak2tuviD1I88eec4w1eE2GFHOrdDS9wNfakWXJtuEEA1hqJsulZ9KsDPZRKuuV2wnvnJUKYYM_RKcN0iu52Z36boXn4_pOt8p6ejM9vKtFrEX1Knz8Sh46O4IVurcIdj4wJUS6avmRYYHjNOFl0O4dOlGiVmvsKq_vkvhFrcpXqiFgt9-OYk1mtz5YCuaTpl0wFmcmW11qUxfhOit9RqBSW2c3FkrjI9NWRivuc9HutcF2_wSFRapSViOlJz9262I7vQchKG9VURgdfXVfmQY1tE4R5iF4aT-ruY6cQf0-j6QAAAAGFpL8IAA", None)
STRING5 = getenv("BQHHYkkAuz2l7z7APDam5Q02nLKDHxA6xH_ieN9ReqV3S2tu_Ak2tuviD1I88eec4w1eE2GFHOrdDS9wNfakWXJtuEEA1hqJsulZ9KsDPZRKuuV2wnvnJUKYYM_RKcN0iu52Z36boXn4_pOt8p6ejM9vKtFrEX1Knz8Sh46O4IVurcIdj4wJUS6avmRYYHjNOFl0O4dOlGiVmvsKq_vkvhFrcpXqiFgt9-OYk1mtz5YCuaTpl0wFmcmW11qUxfhOit9RqBSW2c3FkrjI9NWRivuc9HutcF2_wSFRapSViOlJz9262I7vQchKG9VURgdfXVfmQY1tE4R5iF4aT-ruY6cQf0-j6QAAAAGFpL8IAA", None)

# Bot introduction messages - These can be customized as per your preference
AYU = [
    "💞", "𝚃𝙷𝙸𝚂 𝚂𝙾𝙽𝙶 𝙸𝚂 𝚃𝙾𝚃𝙰𝙻𝙻𝚈 𝙵𝙰𝙱𝚄𝙻𝙰𝚂𝚃𝙸𝙲...🔥🥰", "🔍", "🧪", "ʜᴏʟᴅ ᴏɴ ᴅᴀʀʟɪɴɢ 💗", "⚡️", "🔥", "ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...❤‍🔥", "🎩", "🌈", "🍷", "🥂", "🎲", "🥃", 
    "ᴀᴄᴄʜɪ ᴘᴀsᴀɴᴅ ʜᴀɪ 🥰", "ʟᴏᴏᴋɪɴɢ ғᴏʀ ʏᴏᴜʀ sᴏɴɢ... ᴡᴀɪᴛ! 💗", "🪄", "💌", "ᴏᴋ ʙᴀʙʏ ᴡᴀɪᴛ😘 ғᴇᴡ sᴇᴄᴏɴᴅs", "ᴀʜʜ! ɢᴏᴏᴅ ᴄʜᴏɪᴄᴇ ʜᴏʟᴅ ᴏɴ...",  
    "ᴡᴏᴡ! ɪᴛ's ᴍʏ ғᴀᴠᴏʀɪᴛᴇ sᴏɴɢ...", "ɴɪᴄᴇ ᴄʜᴏɪᴄᴇ..! ᴡᴀɪᴛ 𝟸 sᴇᴄᴏɴᴅ", "🔎", "🍹", "🍻", "ɪ ʟᴏᴠᴇ ᴛʜᴀᴛ sᴏɴɢ..!😍", "💥", "💗", "✨"
]

AYUV = [
    "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 👑 ➪ [🇲𝗥  🇧𝗥𝗢𝗞𝗘𝗡](https://t.me/Aboutbrokenx)",
    "ʜɪɪ, {0} ~\n\n◆ ɪ'ᴍ ᴀ {1} ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴜꜱᴇꜰᴜʟ\n◆ ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\n✨ ꜰᴇᴀᴛᴜʀᴇꜱ ⚡️\n◆ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.\n◆ Sᴜᴘᴇʀғᴀsᴛ ʟᴀɢ Fʀᴇᴇ ᴘʟᴀʏᴇʀ.\n◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ.\n◆ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ.\n◆ ɴᴏ ᴘʀᴏᴍᴏ.\n◆ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.\n◆ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.\n◆ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵.\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 👑 ➪ [🇲𝗥  🇧𝗥𝗢𝗞𝗘𝗡](https://t.me/Aboutbrokenx)",
    "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 👑 ➪ [🇲𝗥  🇧𝗥𝗢𝗞𝗘𝗡](https://t.me/Aboutbrokenx)",
    "ʜɪɪ, {0} ~\n\n◆ ɪ'ᴍ ᴀ {1} ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴜꜱᴇꜰᴜʟ\n◆ ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\n✨ ꜰᴇᴀᴛᴜʀᴇꜱ ⚡️\n◆ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.\n◆ Sᴜᴘᴇʀғᴀsᴛ ʟᴀɢ Fʀᴇᴇ ᴘʟᴀʏᴇʀ.\n◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ.\n◆ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ.\n◆ ɴᴏ ᴘʀᴏᴍᴏ.\n◆ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.\n◆ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.\n◆ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵.\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 👑 ➪ [🇲𝗥  🇧𝗥𝗢𝗞𝗘𝗡](https://t.me/Aboutbrokenx)",
    "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 👑 ➪ [🇲𝗥  🇧𝗥𝗢𝗞𝗘𝗡](https://t.me/Aboutbrokenx)"
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/ca3c86842fe3a4f07a3b6.jpg"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "https://telegra.ph/file/4f0a703ae7b10a7049c61.mp4"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/ca3c86842fe3a4f07a3b6.jpg"
STATS_VID_URL = "https://telegra.ph/file/4f0a703ae7b10a7049c61.mp4"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8ba38eca9318beb6dcede.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/470d98e37b15e7ccdc266.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/c86b07e9972126c769b63.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/470d98e37b15e7ccdc266.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/470d98e37b15e7ccdc266.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/8ba38eca9318beb6dcede.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/8ba38eca9318beb6dcede.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/8ba38eca9318beb6dcede.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
