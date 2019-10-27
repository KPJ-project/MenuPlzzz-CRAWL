from django.urls import path
from . import views

urlpatterns = [
    path('crawl/', views.crawl, name='crawl'),
    path('subway/', views.crawl_subway, name='subway'),
    path('momstouch/', views.crawl_momstouch, name='momstouch'),
    path('popeyes/', views.crawl_popeyes, name='popeyes'),
    path('lotteria/', views.crawl_lotteria, name='lotteria'),


]
