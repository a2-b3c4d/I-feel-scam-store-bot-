import pyrogram.utils
from bot import Bot

# Ensure the correct MIN_CHANNEL_ID value
pyrogram.utils.MIN_CHANNEL_ID = -1002256509918

# Run the bot
if __name__ == "__main__":
    Bot().run()
