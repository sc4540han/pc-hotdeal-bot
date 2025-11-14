import asyncio, yaml, logging, time
from pathlib import Path
from bot.telegram_bot import TelegramBot
from crawler.base import BaseCrawler
from utils.filter import is_pc_part
from utils.message import format_message

import importlib

CONFIG_PATH = Path(__file__).resolve().parents[1] / 'config.yaml'

async def run_crawler(target, bot, storage):
    crawler_cls = getattr(importlib.import_module('crawler.' + target['class'].lower().replace('crawler','')), target['class'])
    crawler = crawler_cls(target['url'])
    try:
        new_articles = await crawler.crawl()
    except Exception as e:
        logging.exception('crawl error %s', target['name'])
        return
    for a in new_articles:
        # a is expected to have: title, url, site, price (opt)
        if not is_pc_part(a.get('title',''), a.get('content','')):
            continue
        key = a.get('url')
        if key in storage:
            continue
        storage.add(key)
        txt = format_message(a)
        await bot.send_message(txt)

async def main():
    logging.basicConfig(level=logging.INFO)
    cfg = yaml.safe_load(open(CONFIG_PATH))
    bot = TelegramBot(cfg['bot']['token'], cfg['bot']['chat_id'])
    storage = set()
    targets = cfg['crawling']['targets']
    interval = cfg['crawling'].get('interval_seconds', 60)
    while True:
        tasks = [run_crawler(t, bot, storage) for t in targets]
        await asyncio.gather(*tasks)
        await asyncio.sleep(interval)

if __name__ == '__main__':
    asyncio.run(main())
