from django.http import JsonResponse, HttpResponse

from .models import Menu
from .utils import macdonald

def crawl(request):
    for category_id in [10,11,13,14,15,16]:
        print(utils.macdonald(category_id))

    #여기에 DB에 bulk Save 하는 코드 구현 필요

    JsonResponse({"Succes":True})
