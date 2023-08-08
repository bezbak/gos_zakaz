from django.shortcuts import render
from .models import Team, Struct, MainInfo, Tourism
# Create your views here.

def managment(request):
    team = Team.objects.all()
    context = {
        'team':team
    }
    return render(request, 'rukovodstvo.html', context)

def structs(request):
    struct = Struct.objects.all()
    context = {
        'struct':struct
    }
    return render(request, 'struktura.html', context)

def main_info(request):
    main_info = MainInfo.objects.latest('id')
    context = {
        'main_info':main_info
    }
    return render(request, 'mainInfo.html',context)

def tourism(request):
    tourism = Tourism.objects.latest('id')
    context = {
        'tourism':tourism
    }
    return render(request, 'tourism.html',context)

def maps(request):
    return render(request, 'maps.html')
