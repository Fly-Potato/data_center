from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpRequest
from django.views import View


def index():
    pass


class Material(View):
    def get(self, request: HttpRequest):
        pass

    def post(self, request: HttpRequest):
        pass
