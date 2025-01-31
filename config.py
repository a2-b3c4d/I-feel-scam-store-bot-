import os
import logging
from logging.handlers import RotatingFileHandler

# Bot Token from @BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "0"))  # Defaults to 0 to prevent errors

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your Database Channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002256509918"))

# Owner Info
OWNER = os.environ.get("OWNER", "Tharun_stryker")
OWNER_ID = int(os.environ.get("OWNER_ID", "6586630448"))

# Owner Username (without '@')
OWNER_USER = os.environ.get("OWNER_USER", "").strip()

# Port
PORT = int(os.environ.get("PORT", "8030"))

# Database Config
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster8")

# Force Subscribe Channel
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002306307006"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002306870616"))

# Number of Bot Workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Default Images
START_PIC = os.environ.get("START_PIC", "https://iili.io/2QFefUb.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://iili.io/2QFefUb.jpg")

# Help Text
HELP_TXT = """<b>ᴛʜɪs ɪs ᴀ ᴍᴏᴠɪᴇ ʙᴏᴛ ғᴏʀ @OutlawBots.

❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs:
├ /start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
├ /about : ɪɴғᴏ ᴀʙᴏᴜᴛ ʙᴏᴛ
└ /help : ʜᴏᴡ ᴛᴏ ᴜsᴇ ʙᴏᴛ

ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟs & ɢᴇᴛ ᴍᴏᴠɪᴇs ғᴏʀ ғʀᴇᴇ! 🎥
ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href="https://t.me/HateXfree">ᯓ ʜᴀᴛᴇ ғʀᴇᴇ ᡣ𐭩</a></b>"""

# About Text
ABOUT_TXT = f"""<b>
╭───────────⍟
├➤ ᴄʀᴇᴀᴛᴏʀ: <a href="https://t.me/InkaLinks">ᴛʜɪs ᴘᴇʀsᴏɴ</a>
├➤ ʟɪʙʀᴀʀy: <a href="https://github.com/pyrogram">ᴘʏʀᴏɢʀᴀᴍ</a>
├➤ ʟᴀɴɢᴜᴀɢᴇ: <a href="https://www.python.org">ᴘʏᴛʜᴏɴ 3</a>
├➤ ᴍʏ ᴜᴘᴅᴀᴛᴇs: <a href="https://t.me/AniHorizon">AniHorizon</a>
├➤ ᴘᴀɪᴅ ʙᴏᴛ: <a href="https://t.me/ifeelscam">ᯓ ɪɴᴠᴀʟɪᴅ ᡣ𐭩</a>
├➤ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href="https://t.me/Tharun_stryker">ᯓ Strykerᡣ𐭩</a>
╰───────────────⍟</b>"""

# Start Message
START_MSG = os.environ.get("START_MESSAGE", "<b>Oi {first}!\n\n<blockquote>😏 I'm a file store bot! I keep private files safe in a specified channel, and others can access them through a special link! 📂🔗</blockquote></b>")

# Admin List
try:
    ADMINS = [OWNER_ID]
    admin_list = os.environ.get("ADMINS", "5115691197 6273945163 6103092779 5231212075").split()
    ADMINS.extend([int(x) for x in admin_list if x.isdigit()])
except ValueError:
    raise Exception("Your Admins list contains invalid data.")

# Force Subscribe Message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Oi! {mention}\n\n<b>😏 Join our channels first! Then click 'Try Again' to get your file! 🏴‍☠️💰.</b>"
)

# Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @AniHorizon</b>")

# Protect Content (Prevent Forwarding)
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False").lower() == "true"

# Disable Share Button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False").lower() == "true"

# Bot Stats
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# User Reply Text
USER_REPLY_TEXT = "❌ Oi! 😡 Don't send me messages directly! 😤 I'm just a file share bot, not your personal assistant! 🏴‍☠️💰"

# Add Extra Admins
ADMINS.append(5191566338)

# Logging
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
