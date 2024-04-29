# news_parser.py
from bs4 import BeautifulSoup
import requests


def parse_news():
    url = 'https://www.unian.net'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        news_list = []
        for news_item in soup.find_all('div', class_='news-item'):
            title_element = news_item.find('h2')
            content_element = news_item.find('p')
            if title_element and content_element:
                title = title_element.text.strip()
                content = content_element.text.strip()
                news_list.append({'title': title, 'content': content})
                print(f"Title: {title}\nContent: {content}\n")
        return news_list
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return None

