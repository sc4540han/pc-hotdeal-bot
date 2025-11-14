from datetime import datetime
def format_message(article: dict) -> str:
    title = article.get('title','상품명 없음')
    price = article.get('price') or article.get('price_text') or '가격 정보 없음'
    site = article.get('site','unknown')
    url = article.get('url','')
    posted = article.get('time') or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return (
        f"🔥 PC 부품 핫딜 감지!\n\n"
        f"상품: {title}\n"
        f"가격: {price}\n"
        f"사이트: {site}\n"
        f"게시글 제목: {title}\n"
        f"링크: {url}\n\n"
        f"⌛ 시간: {posted}"            )
