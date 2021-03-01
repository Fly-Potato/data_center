"""
莱莎2相关
"""
from django.views import View
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
import json
from .models import Material as MaterialModel


# 素材
class Material(View):
    def get(self, request: HttpRequest):
        return HttpResponse('get')

    def post(self, request: HttpRequest):

        data = json.loads(request.body)
        try:
            text = data['text']
        except KeyError:
            res = dict(code=0, info='KeyError')
        else:
            text = str(text)
            text = text.replace('<p>', '')
            text = text.replace('</p>', '')
            text = text.replace('\t', '')
            lines = text.split('\n')
            for line in lines:
                if line.strip():
                    info_list = line.split(' ')
                    if len(info_list) >= 6:
                        try:
                            MaterialModel.objects.get(name=info_list[0])
                        except MaterialModel.DoesNotExist:
                            material_model = MaterialModel()
                        else:
                            continue
                        material_model.name = info_list[0]
                        material_model.level = info_list[1]
                        material_model.attribute = info_list[2]
                        material_model.attribute_num = info_list[3]
                        material_model.type = info_list[4]
                        addrs = []
                        for addr in info_list[5:]:
                            addrs += addr + ' '
                        material_model.addr = addrs
                        try:
                            material_model.save()
                        except ValueError:
                            print(info_list)
                            continue
                    else:
                        print(info_list)
            res = dict(code=1, info='KeyError')
        return JsonResponse(res)
