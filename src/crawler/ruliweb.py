from .base import BaseCrawler
from bs4 import BeautifulSoup as BS
class RuliwebCrawler(BaseCrawler):
    async def parse(self, html):
        soup = BS(html, 'html.parser')
        items = []
        for a in soup.select('a.subject')[:10]:
            title = a.get_text(strip=True)
            href = a.get('href','')
            if href and href.startswith('/'):
                href = 'https://bbs.ruliweb.com' + href
            items.append({'title':title,'url':href,'site':'ruliweb'})
        return items
