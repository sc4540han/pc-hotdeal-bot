from .base import BaseCrawler
from bs4 import BeautifulSoup as BS
class PpomppuCrawler(BaseCrawler):
    async def parse(self, html):
        soup = BS(html, 'html.parser')
        items = []
        for a in soup.select('a.subject_link')[:10]:
            title = a.get_text(strip=True)
            href = a.get('href','')
            if href and not href.startswith('http'):
                href = 'https://www.ppomppu.co.kr' + href
            items.append({'title':title,'url':href,'site':'ppomppu'})
        return items
