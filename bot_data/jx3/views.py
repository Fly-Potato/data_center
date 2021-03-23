from django.views import View
from django.http import JsonResponse, HttpRequest
from datetime import date


class RiChang(View):
    def get(self, request: HttpRequest):
        start_datetime = date(2021, 1, 1)
        days = date.today() - start_datetime
        dazhan = ['1', '2', '3']
        print(dazhan[days.days % len(dazhan)])
