from django.db import models


class TimeStampedModel(models.Model):
    '''
    모든 모델에 공통적으로 사용되는
    createdDate, updatedDate 부분을 따로 추상화 시켜서 추상 클래스화 한다.
    '''
    created_date = models.DateTimeField(("생성 시간"), auto_now_add=True)
    updated_date = models.DateTimeField(("수정 시간"), auto_now=True)

    # 추상 클래스로 지정
    class Meta:
        abstract = True


class StoreType(TimeStampedModel):
    name = models.CharField(("가게 타입"), max_length=100)


class Store(TimeStampedModel):
    name = models.CharField(("가게 이름"), max_length=100)
    image = models.CharField(("이미지"), max_length=200, null=True, blank=True)
    storetype = models.ForeignKey(
        StoreType, verbose_name=("가게 종류"), on_delete=models.CASCADE)


class Category(TimeStampedModel):
    name = name = models.CharField(("메뉴 카테고리"), max_length=100)
    store = models.ForeignKey(Store, verbose_name=(
        "가게 id"), on_delete=models.CASCADE)


class Menu(TimeStampedModel):
    name = models.CharField(("메뉴 이름"), max_length=100)
    is_event = models.BooleanField(("행사 중인가?"), default=False)
    price = models.CharField(("가격"), max_length=50, default="")
    event_price = models.CharField(("행사 가격"), max_length=50, default="")
    image = models.CharField(("상품 이미지"), max_length=100)
    is_selling = models.BooleanField(("아직 파는 중인가?"), default=True)
    category = models.ForeignKey(Category, verbose_name=(
        "카테고리 id"), on_delete=models.CASCADE)
    store = models.ForeignKey(Store, verbose_name=(
        "가게 id"), on_delete=models.CASCADE)
