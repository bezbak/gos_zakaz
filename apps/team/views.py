from django.shortcuts import render
from .models import Team, Struct, MainInfo, Tourism, Links
# Create your views here.

def managment(request):
    team = Team.objects.all()
    links = Links.objects.latest('id')
    context = {
        'team':team,
        'links':links,
    }
    return render(request, 'rukovodstvo.html', context)

def structs(request):
    struct = Struct.objects.all()
    links = Links.objects.latest('id')
    context = {
        'struct':struct,
        'links':links,

    }
    return render(request, 'struktura.html', context)

def main_info(request):
    main_info = MainInfo.objects.latest('id')
    links = Links.objects.latest('id')
    context = {
        'main_info':main_info,
        'links':links,

    }
    return render(request, 'mainInfo.html',context)

def tourism(request):
    tourism = Tourism.objects.latest('id')
    links = Links.objects.latest('id')
    context = {
        'tourism':tourism,
        'links':links,

    }
    return render(request, 'tourism.html',context)

def maps(request):
    links = Links.objects.latest('id')
    context = {
        'links':links,

    }
    return render(request, 'maps.html',context)
