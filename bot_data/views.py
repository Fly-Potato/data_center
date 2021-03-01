from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpRequest
from django.views import View


def index(request: HttpRequest):
    return render(request, 'bot_data/index.html')


