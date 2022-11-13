from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    news_list = sorted(
        news_list,
        key=lambda new: new["comments_count"],
        reverse=True,
    )

    top_5 = [(new["title"], new["url"]) for new in news_list[:5]]
    return top_5


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
