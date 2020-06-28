from django.shortcuts import render

# Create your views here.

def places(request):
    content = {}
    return render(request, 'map/map.html', content)