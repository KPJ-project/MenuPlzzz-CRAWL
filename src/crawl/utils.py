from ast import literal_eval
from bs4 import BeautifulSoup
import requests


def macdonald(page):
    '''
    맥도날드 페이지에서, 메뉴들을 크롤링 해온다.
    '''

    # url, header 설정
    url = "https://www.mcdelivery.co.kr/kr/browse/menu.html?daypartId=2&catId={}".format(
        page)
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    # 응답 값을 받아오고, bs 객체로 변환한다.
    response = requests.get(url, headers={"USER-AGENT": u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    # 상품부분에 해당하는 부분을 find, find_all로 필터링 한다.
    products_box_soup = soup.find("div", {"id": "product-cards"})
    products = products_box_soup.find_all(
        "a", {"class": "btn btn-block action-create btn-yellow"})

    # 필터링 된 정보를 재가공 한다.
    informations = []
    for product in products:
        data = product.get('onclick')
        if data.startswith('onProductClick'):
            informations.append(data[len('onProductClick('): -1])

    result = []
    for information in informations:
        temp_dict = {}
        menu = literal_eval(information)
        temp_dict['store'] = "맥도날드"
        temp_dict['name'] = menu['name']
        temp_dict['price'] = menu['price'][2:]
        temp_dict['category'] = menu['cat']
        result.append(temp_dict)

    return result


def subway():
    '''
    서브웨이 페이지에서, 메뉴들을 크롤링 해온다.
    '''

    # url, header 설정
    url = "http://subway.co.kr/sandwichList"
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    # 응답 값을 받아오고, bs 객체로 변환한다.
    response = requests.get(url, headers={"USER-AGENT": u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    category = {
        'new': '신제품',
        'promotion': '프로모션',
        'cl': '클래식',
        'fl': '프레쉬&라이트',
        'pl': '프리미엄',
        'bf': '아침메뉴',
    }

    result = []
    for k, v in category.items():
        products = soup.find_all("li", {'class': '{}'.format(k)})

        for product in products:
            image = product.img.get('src')
            name = product.img.get('alt')

            temp_dict = {}
            temp_dict['name'] = name
            temp_dict['price'] = ""
            temp_dict['category'] = v
            temp_dict['image'] = image.replace("..", "http://subway.co.kr")
            result.append(temp_dict)

    return result
