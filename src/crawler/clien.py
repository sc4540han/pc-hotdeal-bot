from .base import BaseCrawler
from bs4 import BeautifulSoup as BS
class ClienCrawler(BaseCrawler):
    async def parse(self, html):
        soup = BS(html, 'html.parser')
        items = []
        for a in soup.select('a.list_subject')[:10]:
            title = a.get_text(strip=True)
            href = a.get('href','')
            if href and href.startswith('/'):
                href = 'https://www.clien.net' + href
            items.append({'title':title,'url':href,'site':'clien'})
        return items
