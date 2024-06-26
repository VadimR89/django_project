from django.shortcuts import render
from .news_parser import parse_news
from .currency_parser import get_currency_rates


def display_requests_page(request):
    news = parse_news()
    currency_rates = get_currency_rates()
    return render(request, 'requests_page.html', {'news': news, 'currency_rates': currency_rates})


def main(request):
    return render(request, 'Newsapp/index.html')
