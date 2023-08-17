from django.urls import path
from .views import structs, managment, main_info, maps, tourism,corruption, managment_detail
urlpatterns = [
    path('managment/', managment, name='managment'),
    path('managment/<str:full_name>/', managment_detail, name='managment_detail'),
    path('structs/', structs, name='structs'),
    path('main_info/', main_info, name='main_info'),
    path('tourism/', tourism, name='tourism'),
    path('corruption/', corruption, name='corruption'),
    path('maps/', maps, name='maps'),
]
