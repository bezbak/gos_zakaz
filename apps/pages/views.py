from django.shortcuts import render
from apps.team.models import Links, GosLinks,Images
from apps.pages.models import Police, DevFund, StateSymbols
# Create your views here.

def policy(request):
    policy_text = Police.objects.latest('id')
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'policy_text':policy_text,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }

    return render(request, "police.html", context)

def devfund(request):
    devfund_text = DevFund.objects.latest('id')
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'devfund_text':devfund_text,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }

    return render(request, "police.html", context)

def state_symbols(request):
    state_symbols_text = StateSymbols.objects.latest('id')
    links = Links.objects.latest('id')
    images = Images.objects.latest('id')
    gos_links = GosLinks.objects.all()
    context = {
        'state_symbols_text':state_symbols_text,
        'links':links,
        'gos_links':gos_links,
        'images':images,
    }

    return render(request, "police.html", context)

