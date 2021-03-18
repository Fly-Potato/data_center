from django.shortcuts import render
from django.views import View
from django.http import HttpRequest


def login(request: HttpRequest):
    return render(request, 'login/index.html')
