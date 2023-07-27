from django.urls import path
from apps.news.views import index, all_news, search

urlpatterns = [
    path('', index, name='index'),
    path('all_news/', all_news, name='all_news'),
    path('search/', search, name='search'),
]
