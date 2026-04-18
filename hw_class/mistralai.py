import requests
from datetime import datetime, timedelta
from api_methods import get_everything
from config import NEWS_API_KEY, MISTRAL_API_KEY


def past_week_digest(news_api_key, mistral_api_key, q):
    # Берем новости за последние 7 дней
    week_ago = str(datetime.now() - timedelta(days=7))[:10]
    today = str(datetime.now())[:10]

    data = get_everything(api_key=news_api_key, q=q, w_from=week_ago, to=today)
    articles = data.get('articles', [])[:20]

    if not articles:
        return "Новостей за последнюю неделю не найдено."

    all_news = ""
    for a in articles:
        t = a.get('title')
        d = a.get('description')
        if t and d:
            all_news += f"{t}. {d}\n"

    prompt = (
        f"Вот новости про {q} за последнюю неделю:\n{all_news}\n"
        f"Сделай по ним краткую выжимку на русском, примерно 250-300 слов. "
        f"Просто перескажи самое важное сплошным текстом, без маркеров и разделений на блоки."
    )

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {mistral_api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mistral-small-latest",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=body)
    res_json = response.json()

    report_text = res_json['choices'][0]['message']['content']

    return f"**Краткая выжимка по представленным статьям (250-300 слов):**\n\n{report_text}"


def save_to_txt(topic, text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == '__main__':
    topic = "servals"

    print(f"Ищу новости про сервалов за последнюю неделю...")

    report = past_week_digest(NEWS_API_KEY, MISTRAL_API_KEY, topic)
    save_to_txt(topic, report)

    print("Готово! Отчет записан в файл result.txt")