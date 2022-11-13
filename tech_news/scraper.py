import time
import requests
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
