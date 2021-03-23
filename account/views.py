from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json
import requests


def login(request: HttpRequest):
    return render(request, 'login/index.html')


@require_http_methods(['GET', 'POST'])
def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        if request.body:
            _json = json.loads(request.body)
            token = _json.get('token', '')
            if token:
                data = {
                    'secret': settings.reCAPTCHA,
                    'response': token
                }
                recaptcha = requests.post('https://recaptcha.net/recaptcha/api/siteverify', data=data).json()
                if recaptcha['success'] == 'true':
                    return JsonResponse(dict(code=1))
            return JsonResponse(dict(code=0))
