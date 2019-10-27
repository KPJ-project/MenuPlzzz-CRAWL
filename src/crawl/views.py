from django.http import JsonResponse, HttpResponse

from .models import Menu, Category, Store
from .utils import macdonald, subway, momstouch, popeyes, lotteria


def crawl(request):
    menu_list = []

    # 각 카테코리별로 크롤링을 해온다.
    for category_id in [10, 11, 13, 14, 15, 16]:
        # 크롤링 해온 json return 값 상에서, 각 menu를 DB에 저장한다
        for menu in macdonald(category_id):
            category = Category.objects.get(name=menu['category'])
            store = Store.objects.get(name=menu['store'])

            # menu 객체를 만들고, 리스트에 추가한다.
            menu_object = Menu(
                name=menu['name'],
                price=menu['price'],
                category=category,
                store=store,
                image=menu['image']
            )

            menu_list.append(menu_object)

    # menu 객체를 한번에 db에 create 한다.
    Menu.objects.bulk_create(menu_list)

    return JsonResponse({"Succes": True})


def crawl_subway(request):
    menu_list = []

    # 각 카테코리별로 크롤링을 해온다.
    for category in ['sandwichList', 'saladList', 'toppingList', 'sideDrink', 'catering']:
        # 크롤링 해온 json return 값 상에서, 각 menu를 DB에 저장한다
        for menu in subway(category):
            print(menu['category'])
            category = Category.objects.get(name=menu['category'])
            store = Store.objects.get(name=menu['store'])

            # menu 객체를 만들고, 리스트에 추가한다.
            menu_object = Menu(
                name=menu['name'],
                image=menu['image'],
                price=menu['price'],
                category=category,
                store=store)

            menu_list.append(menu_object)

    Menu.objects.bulk_create(menu_list)

    return JsonResponse({"Succes": True})


def crawl_momstouch(request):
    menu_list = []

    for category_id in [1, 4, 5, 6]:
        for menu in momstouch(category_id):

            category = Category.objects.get(name=menu['category'])
            store = Store.objects.get(name=menu['store'])

            menu_object = Menu(
                name=menu['name'],
                image=menu['image'],
                price=menu['price'],
                category=category,
                store=store
            )
            menu_list.append(menu_object)
    Menu.objects.bulk_create(menu_list)

    return JsonResponse({"Succes": True})


def crawl_popeyes(request):
    menu_list = []

    for category_id in [123]:
        for menu in popeyes(category_id):
            category = Category.objects.get(
                name=menu['category'], store__name='파파이스')
            store = Store.objects.get(name=menu['store'])

            menu_object = Menu(
                name=menu['name'],
                image=menu['image'],
                price=menu['price'],
                category=category,
                store=store
            )
            menu_list.append(menu_object)
    Menu.objects.bulk_create(menu_list)

    return JsonResponse({"Succes": True})

    # def crawl_subway(request):
    #     menu_list = []

    #     # 각 카테코리별로 크롤링을 해온다.
    #     for cate in ['sandwichList', 'saladList', 'toppingList', 'sideDrink', 'catering']:
    #         # 크롤링 해온 json return 값 상에서, 각 menu를 DB에 저장한다
    #         for menu in subway(cate):
    #             print(menu['name'])
    #             Menu.objects.filter(name=menu['name']).update(image=menu['image'])

    #     return JsonResponse({"Succes": True})


def crawl_lotteria(request):
    menu_list = []

    for menu in lotteria():
        print(menu)
        category = Category.objects.get(
            name=menu['category'], store__name='롯데리아'
        )
        store = Store.objects.get(name=menu['store'])

        menu_object = Menu(
            name=menu['name'],
            image=menu['image'],
            price=menu['price'],
            category=category,
            store=store
        )
        menu_list.append(menu_object)
    Menu.objects.bulk_create(menu_list)
    return JsonResponse({"Succes": True})
