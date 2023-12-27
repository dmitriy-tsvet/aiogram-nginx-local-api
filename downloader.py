from aiogram import Bot
from aiogram.types import Downloadable
import aiohttp
import re
import aiofiles


class NginxAPIDownloader:
    def __init__(self, bot: Bot, url: str):
        self.bot = bot
        self.url = url

    async def download(self, file: str | Downloadable, destination) -> str:
        try:
            await self.bot.download(file, destination)
        except OSError as e:
            server_filepath = re.findall(r"\'(.+)\'", str(e))[0]

            async with aiohttp.ClientSession() as session:
                async with session.get(self.url+server_filepath) as file:
                    file = await file.content.read()
                    async with aiofiles.open(destination, "wb") as f:
                        await f.write(file)
        return destination
