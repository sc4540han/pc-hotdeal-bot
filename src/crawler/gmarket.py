from .base import BaseCrawler
from bs4 import BeautifulSoup as BS
class GmarketCrawler(BaseCrawler):
    async def parse(self, html):
        soup = BS(html, 'html.parser')
        items = []
        for a in soup.select('a')[:10]:
            title = a.get_text(strip=True)
            href = a.get('href','')
            items.append({'title':title,'url':href,'site':'gmarket'})
        return items
