from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpRequest
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import VersionModel
from django.forms import model_to_dict


@login_required
def index(request: HttpRequest):
    return render(request, 'bot_data/index.html')


class VersionInfo(View):
    def get(self, request: HttpRequest):
        module = request.GET.get('module', '')
        if module:
            try:
                version_info = VersionModel.objects.get(name=module)
            except VersionModel.DoesNotExist:
                return JsonResponse(dict(code=0, info="module not found!"))
            else:
                return JsonResponse(dict(code=1, version_info=model_to_dict(version_info)))
        else:
            versions_info = []
            for version in VersionModel.objects.all().values():
                versions_info.append(version)
            return JsonResponse(dict(code=1, version_info=versions_info))
