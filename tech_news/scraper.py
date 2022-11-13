import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    titles = selector.css("a.cs-overlay-link::attr(href)").getall()
    return titles


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    try:
        next_page_link = selector.css("a.next::attr(href)").get()
    except requests.HTTPError:
        return None
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    page_info = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css("span.author > a ::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip(),
        "tags": selector.css("section.post-tags ul li a::text").getall(),
        "category": selector.css("span.label::text").get(),
    }
    return page_info


# Requisito 5
def get_tech_news(amount):
    news_blog = fetch("https://blog.betrybe.com/")
    scrape = scrape_novidades(news_blog)
    news = list()

    while amount > 0:
        news_page = fetch(scrape[amount - 1])
        news.append(scrape_noticia(news_page))
        amount -= 1

    if amount > 0:
        next_page_link = scrape_next_page_link(news_blog)
        news_blog = fetch(next_page_link)
        scrape = scrape_novidades(news_blog)

    create_news(news)
    return news
