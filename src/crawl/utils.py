from ast import literal_eval
from bs4 import BeautifulSoup
import requests


from ast import literal_eval
from bs4 import BeautifulSoup
import requests


def macdonald(page):
    '''
    맥도날드 페이지에서, 메뉴들을 크롤링 해온다.
    '''
    category = {
        10: "추천 메뉴",
        11: "버거 & 세트",
        13: "스낵 & 사이드",
        14: "음료",
        15: "디저트",
        16: "해피밀®"
    }

    # url, header 설정
    url = "https://www.mcdelivery.co.kr/kr/browse/menu.html?daypartId=1&catId={}".format(
        page)
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    # 응답 값을 받아오고, bs 객체로 변환한다.
    response = requests.get(url, headers={"USER-AGENT": u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    # 상품부분에 해당하는 부분을 find, find_all로 필터링 한다.
    products_box_soup = soup.find_all("div", {"class": "panel-product"})

    result = []

    for product in products_box_soup:
        temp_dict = {}
        image_soup = product.find("img", {"class": "img-block"})
        image = image_soup.get("src")

        title_soup = product.find("h5", {"class": "product-title"})
        title = title_soup.text

        price_soup = product.find("span", {"class": "starting-price"})
        price = price_soup.text[2:]

        temp_dict['name'] = title
        temp_dict['price'] = price
        temp_dict['image'] = image
        temp_dict['store'] = "맥도날드"
        temp_dict['category'] = category.get(page)
        result.append(temp_dict)
    return result


def subway(category):
    '''
    서브웨이 페이지에서, 메뉴들을 크롤링 해온다.
    '''

    # url, header 설정
    url = "http://subway.co.kr/{}".format(category)
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    cate = {
        'sandwichList': "샌드위치",
        'saladList': "찹샐러드",
        'toppingList': "추가토핑",
        'sideDrink': "사이드 / 음료",
        'catering': "단체메뉴",
    }

    # 응답 값을 받아오고, bs 객체로 변환한다.
    response = requests.get(url, headers={"USER-AGENT": u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    result = []

    products = soup.find_all("img")

    for product in products:
        if product.get('alt') is not None:
            temp_dict = {}
            temp_dict['store'] = '서브웨이'
            temp_dict['name'] = product.get("alt")
            temp_dict['price'] = ""
            temp_dict['category'] = cate.get(category)
            temp_dict['image'] = product.get(
                "src").replace("..", "http://subway.co.kr")
            result.append(temp_dict)

    return result


def momstouch(menu):
    '''
    맘스터치 페이지에서, 메뉴들을 크롤링 해온다.
    '''

    result = []
    menu_page = []
    for page in range(1, 100):
        # url, header 설정
        url = "http://www.momstouch.co.kr/sub/menu/menu_list.html?pg={}&menu={}".format(
            page, menu)
        u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

        # 응답 값을 받아오고, bs 객체로 변환한다.
        response = requests.get(url, headers={"USER-AGENT": u_a})
        soup = BeautifulSoup(response.content.decode('euc-kr', 'replace'))

        if "메뉴 준비중입니다" in soup.text:
            break

        products_box_soup = soup.find("div", {"class": "menu_list"})
        products = products_box_soup.find_all("img")
        title = soup.find("strong")

        site_src = "http://www.momstouch.co.kr/"

        for product in products:
            temp_dict = {}
            data = product.get('alt')
            resource = product.get("src")
            if data is not "":
                temp_dict['name'] = data
                temp_dict['category'] = title.text.strip()
                temp_dict['image'] = site_src + resource.replace("../", "")
                temp_dict['price'] = ""
                temp_dict['store'] = '맘스터치'
                menu_page.append(temp_dict)

    return menu_page


def popeyes(page):
    '''
    popeyes 페이지에서, 메뉴들을 크롤링 해온다.
    '''

    # url, header 설정
    url = "http://www.popeyes.co.kr/menu/list.asp?cate={}".format(page)
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    # 응답 값을 받아오고, bs 객체로 변환한다.
    response = requests.get(url, headers={"USER-AGENT": u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    cate = {
        96: '치킨',
        97: '치킨텐더',
        98: '테이크아웃팩',
        123: '버거',
        100: '사이드',
        101: '음료',
        102: '소스',
    }

    products = soup.find_all("div", {'class': 'flavor-details'})

    result = []
    for product in products:
        image = product.img.get("src")
        name = product.img.get("alt")
        category = cate[page]

        temp_dict = {}
        temp_dict['image'] = image
        temp_dict['name'] = name
        temp_dict['category'] = category
        temp_dict['price'] = ""
        temp_dict['store'] = "파파이스"

        result.append(temp_dict)

    return result


def lotteria():
    '''
    lotteria 페이지에서, 메뉴들을 크롤링 해온다.
    '''

    # url, header 설정
    url = "http://www.lotteria.com/menu/Menu_all.asp"
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    # 응답 값을 받아오고, bs 객체로 변환한다.
    response = requests.get(url, headers={"USER-AGENT": u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all("div", {'class': 'h3_group2'})
    products = soup.find_all("div", {'class': 'memu_group'})

    result = []
    title_result = []
    for title in titles:
        title_result.append(title.text)

    result = []
    count = 0
    for product in products:
        for li in product.find_all("li"):
            temp_dict = {}
            temp_dict['image'] = "http://www.lotteria.com" + li.img.get('src')
            temp_dict['name'] = li.img.get('alt')
            temp_dict['price'] = li.strong.text[:-1].replace(",", "")
            temp_dict['store'] = "롯데리아"
            temp_dict['category'] = title_result[count].strip()
            result.append(temp_dict)
        count += 1
    return result
