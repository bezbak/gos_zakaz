from django.shortcuts import render
from apps.team.models import Links, GosLinks,Images
from apps.pages.models import Police, DevFund, StateSymbols, Rayons
# Create your views here.

def policy(request):
    policy_text = Police.objects.last()
    links = Links.objects.last()
    images = Images.objects.last()
    gos_links = GosLinks.objects.all()
    context = {
        'policy_text':policy_text,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }

    return render(request, "police.html", context)

def devfund(request):
    devfund_text = DevFund.objects.last()
    links = Links.objects.last()
    images = Images.objects.last()
    gos_links = GosLinks.objects.all()
    context = {
        'devfund_text':devfund_text,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }

    return render(request, "dev_fund.html", context)

def state_symbols(request):
    state_symbols_text = StateSymbols.objects.last()
    links = Links.objects.last()
    images = Images.objects.last()
    gos_links = GosLinks.objects.all()
    context = {
        'state_symbols_text':state_symbols_text,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }

    return render(request, "state_symbol.html", context)

def rayon_detail(request, id):
    rayon = Rayons.objects.get(id=id)
    links = Links.objects.last()
    images = Images.objects.last()
    gos_links = GosLinks.objects.all()
    context = {
        'rayon':rayon,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }
    return render(request, "rayon.html", context)
    