import aiohttp, asyncio
from bs4 import BeautifulSoup as BS
class BaseCrawler:
    def __init__(self, url):
        self.url = url
    async def fetch(self, session, url):
        async with session.get(url, timeout=20) as resp:
            return await resp.text()
    async def crawl(self):
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, self.url)
            return await self.parse(html)
    async def parse(self, html):
        # Should return list of dict articles: {title,url,site,price,content}
        return []
