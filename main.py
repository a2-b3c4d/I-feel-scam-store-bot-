import asyncio
import pyrogram.utils
from bot import Bot

# Set Pyrogram minimum channel ID
pyrogram.utils.MIN_CHANNEL_ID = -1002256509918

# Function to run the bot properly
def main():
    bot = Bot()
    try:
        loop = asyncio.get_running_loop()  # Check if event loop is already running
        asyncio.ensure_future(bot.start())  # Schedule bot startup
    except RuntimeError:
        loop = asyncio.new_event_loop()  # Create a new event loop if needed
        asyncio.set_event_loop(loop)
        loop.run_until_complete(bot.start())  # Run bot

# Ensure the script runs correctly
if __name__ == "__main__":
    main()
