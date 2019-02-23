from django.http import JsonResponse, HttpResponse

from .models import Menu, Category, Store
from .utils import macdonald

def crawl(request):
    menu_list = []

    #각 카테코리별로 크롤링을 해온다.
    for category_id in [10,11,13,14,15,16]:
        #크롤링 해온 json return 값 상에서, 각 menu를 DB에 저장한다
        for menu in macdonald(category_id):
            category = Category.objects.get(name=menu['category'])            
            store = Store.objects.get(name=menu['store'])

            #menu 객체를 만들고, 리스트에 추가한다.
            menu_object = Menu(
                name=menu['name'], 
                price=menu['price'], 
                category=category, 
                store=store)

            menu_list.append(save_object)
            
    #menu 객체를 한번에 db에 create 한다.
    Menu.objects.bulk_create(menu_list)
    
    return JsonResponse({"Succes":True})
