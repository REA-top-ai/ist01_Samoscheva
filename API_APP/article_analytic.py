import requests as r
url = r.get('https://newsapi.org/v2/everything?apiKey=bab0f95a220a4043b5a07b40b88b1b11&q=servals&pageSize=50&sortBy=publishedAt').json()

result = [
    {
    "title": a["title"],
    "source": a["source"]["name"],
    "published": a["publishedAt"],
    "author": a["author"]
    }
    for a in url["articles"]
    if a["title"] and a["title"].strip()
    and a["url"] and a["url"].startswith("http")
    and a["description"] and len(a["description"]) >= 50
    ]

print(result)
print(f"Количество статей: {len(result)}")