from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search = search_news({"title": {"$regex": title.lower()}})
    news_list = [(news["title"], news["url"]) for news in search]
    return news_list


# Requisito 7
def search_by_date(date):
    try:
        date_search = datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        raise ValueError("Data inválida")

    search = search_news(
        {"timestamp": {"$regex": date_search.strftime("%d/%m/%Y")}}
    )
    news_list = [(news["title"], news["url"]) for news in search]

    return news_list


# Requisito 8
def search_by_tag(tag):
    try:
        search = search_news({"tags": {"$regex": tag.lower().capitalize()}})
        news_list = [(news["title"], news["url"]) for news in search]
    except ValueError:
        news_list = []
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
