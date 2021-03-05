from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views import View
from bot_data.laisha2.models import Material
from django.forms import model_to_dict


class API(View):
    modules = ['laisha2']

    def get(self, request: HttpRequest, module: str):
        if module in self.modules:
            return getattr(self, module)(request.GET.dict())
        return JsonResponse(dict(code=1))

    def laisha2(self, args: dict):
        # print(args)
        return LaiSha2.execute(**args)


class LaiSha2:
    methods = ['get_material_info']
    response = None

    @classmethod
    def execute(cls, **kwargs):
        method = kwargs.get('method')
        if method in cls.methods:
            return getattr(cls, method)(**kwargs)

    @classmethod
    def get_material_info(cls, **kwargs):
        name = kwargs.get('name')
        if name:
            materials = Material.objects.filter(name__contains=name)
            if materials:
                res = list()
                for material in materials:
                    res.append(model_to_dict(material))
                return JsonResponse(dict(code=1, materials=res))

            else:
                return JsonResponse(dict(code=0, info='未查找到相关材料！'))
