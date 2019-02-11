from ast import literal_eval
from bs4 import BeautifulSoup
import requests

def macdonald(page):
    '''
    맥도날드 페이지에서, 메뉴들을 크롤링 해온다.
    '''
    
    #url, header 설정
    url = "https://www.mcdelivery.co.kr/kr/browse/menu.html?daypartId=2&catId={}".format(page)
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    
    #응답 값을 받아오고, bs 객체로 변환한다.
    response = requests.get(url, headers={"USER-AGENT":u_a})
    soup = BeautifulSoup(response.text, 'html.parser')
        
    #상품부분에 해당하는 부분을 find, find_all로 필터링 한다.
    products_box_soup = soup.find("div", {"id":"product-cards"})
    products = products_box_soup.find_all("a", {"class": "btn btn-block action-create btn-yellow"})

    #필터링 된 정보를 재가공 한다.
    informations = []
    for product in products:
        data = product.get('onclick')
        if data.startswith('onProductClick'):
            informations.append(data[len('onProductClick('): -1])
    
    result = []
    for information in informations:
        temp_dict = {}
        menu = literal_eval(information)
        temp_dict['name'] = menu['name']
        temp_dict['price'] = menu['price'][2:]
        temp_dict['category'] = menu['cat']
        result.append(temp_dict)
        
    return result