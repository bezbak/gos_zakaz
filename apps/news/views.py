from django.shortcuts import render, redirect
from apps.news.models import News
from apps.gallery.models import Image
from django.db.models import Q
from apps.team.models import Links, Images, GosLinks
# Create your views here.
def index(request):
    slider_news = News.objects.all().order_by('-id')[:2]
    month_news = News.objects.all().order_by('-id')[3:7]
    slider2_news = News.objects.all()[:12]
    gallery = Image.objects.all()
    links = Links.objects.latest('id')
    gos_links = GosLinks.objects.all()
    images = Images.objects.latest('id')
    context = {
        'slider_news':slider_news,
        'month_news':month_news,
        'slider2_news':slider2_news,
        'gallery':gallery,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }
    return render(request, 'index.html', context)

def all_news(request):
    news = News.objects.all()
    links = Links.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'news':news,
        'links':links,
        'gos_links':gos_links,
        'all_news':True
    }
    return render(request, 'all_news.html', context)

def news_detail(request, id):
    news = News.objects.get(id=id)
    links = Links.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'news':news,
        'links':links,
        'gos_links':gos_links,
    }
    return render(request, 'newsDetails.html', context)

def search(request):
    news = News.objects.all()
    links = Links.objects.latest('id')
    gos_links = GosLinks.objects.all()
    search_key = request.GET.get('search_key')
    if search_key:
        news = News.objects.all().filter(Q(title__icontains = search_key)| Q(description__icontains=search_key))
    context = {
        'news':news,
        'links':links,
        'gos_links':gos_links,
    }
    return render(request, 'search.html', context )
