from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(reqest):
    data = {'title': 'hello my friends',
            'description': 'this project in work'}
    return render(reqest, 'country/index.html', context=data)


def page_not_found(reqest, exception):
    return HttpResponseNotFound('<h1>Page not found 404</h1>')