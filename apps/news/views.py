from django.shortcuts import render
from apps.news.models import News
from apps.gallery.models import Image
from django.db.models import Q
# Create your views here.
def index(request):
    slider_news = News.objects.all().order_by('-id')[:2]
    month_news = News.objects.all().order_by('-id')[3:7]
    slider2_news = News.objects.all()[:12]
    gallery = Image.objects.all()
    context = {
        'slider_news':slider_news,
        'month_news':month_news,
        'slider2_news':slider2_news,
        'gallery':gallery,
    }
    return render(request, 'index.html', context)

def all_news(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request, 'all_news.html', context)

def search(request):
    news = News.objects.all()
    search_key = request.GET.get('search_key')
    if search_key:
        news = News.objects.all().filter(Q(title__icontains = search_key)| Q(description__icontains=search_key))
    context = {
        'news':news
    }
    return render(request, 'search.html', context )