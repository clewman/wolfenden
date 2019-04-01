from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def test(request):
    return HttpResponse('ok')

def index(request):
    return render(request, 'den/index.html')

def urban(request):
    return render(request, 'den/urban.html')

def parallax(request):
    return render(request, 'den/parallax.html')
