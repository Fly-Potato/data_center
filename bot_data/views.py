from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpRequest
from django.views import View
from django.contrib.auth.decorators import login_required


@login_required
def index(request: HttpRequest):
    return render(request, 'bot_data/index.html')


