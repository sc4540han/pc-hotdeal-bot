import asyncio
from telegram import Bot
class TelegramBot:
    def __init__(self, token, chat_id):
        self.bot = Bot(token=token)
        self.chat_id = chat_id
    async def send_message(self, text):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.bot.send_message, self.chat_id, text)
