from django.urls import path
from apps.news.views import index, all_news, search, news_detail,gallery

urlpatterns = [
    path('', index, name='index'),
    path('all_news/', all_news, name='all_news'),
    path('gallery/', gallery, name='gallery'),
    path('search/', search, name='search'),
    path('news_detail/<int:id>/', news_detail, name='news_detail'),
]
