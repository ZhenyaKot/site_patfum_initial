from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин Духов Perfume&Symphonies'
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том какой классный магазин'
    }

    return render(request, 'main/about.html', context)

