from django.urls import path
from .views import structs, managment, main_info, maps, tourism
urlpatterns = [
    path('managment/', managment, name='managment'),
    path('structs/', structs, name='structs'),
    path('main_info/', main_info, name='main_info'),
    path('tourism/', tourism, name='tourism'),
    path('maps/', maps, name='maps'),
]
