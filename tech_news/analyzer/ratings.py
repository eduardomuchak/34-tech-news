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
    news_list = find_news()
    categories = [new["category"] for new in news_list]
    categories_count = {}

    for category in categories:
        if category in categories_count:
            categories_count[category] += 1
        else:
            categories_count[category] = 1

    categories_count_sorted = sorted(
        categories_count,
        key=lambda category: (-categories_count[category], category),
    )

    top_5 = categories_count_sorted[:5]
    return top_5
