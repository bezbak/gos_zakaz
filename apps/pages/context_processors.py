
from .models import Rayons 

def rayons_context(request):
    rayons = Rayons.objects.all()
    return {'rayons': rayons}