from django.urls import path
from apps.pages.views import policy, devfund, state_symbols,rayon_detail

urlpatterns = [
    path('policy/', policy, name='policy'),
    path('devfund/', devfund, name='devfund'),
    path('state_symbols/', state_symbols, name='state_symbols'),
    path('rayon_detail/<int:id>/', rayon_detail, name='rayon_detail'),
]
