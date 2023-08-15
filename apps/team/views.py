from django.shortcuts import render
from .models import Team, Struct, MainInfo, Tourism, Links,Corruption, GosLinks,Images
# Create your views here.

def managment(request):
    team = Team.objects.all()
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'team':team,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }
    return render(request, 'rukovodstvo.html', context)

def structs(request):
    struct = Struct.objects.all()
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'struct':struct,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }
    return render(request, 'struktura.html', context)

def main_info(request):
    main_info = MainInfo.objects.latest('id')
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'main_info':main_info,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }
    return render(request, 'mainInfo.html',context)

def tourism(request):
    tourism = Tourism.objects.latest('id')
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'tourism':tourism,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }
    return render(request, 'tourism.html',context)

def corruption(request):
    corruption = Corruption.objects.latest('id')
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'corruption':corruption,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }
    return render(request, 'corruption.html',context)

def maps(request):
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }
    return render(request, 'maps.html',context)
