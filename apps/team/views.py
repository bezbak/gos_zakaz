from django.shortcuts import render
from .models import Team, Struct
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
    return render(request, 'mainInfo.html')

def maps(request):
    return render(request, 'maps.html')
