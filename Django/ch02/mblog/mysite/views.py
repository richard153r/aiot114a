from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime

# Create your views here.

def index(request):
    posts = Post.objects.all()
    now = datetime.now()
    # return HttpResponse("Hello, world!")
    return render(request, 'index.html', locals())

def showpost(request, slug ,id=1):
    post = Post.objects.get(slug=slug)
    now = datetime.now()
    return render(request, 'showpost.html', locals())

def mptt(request):
    return render(request, 'mqtt-dashboard-temp-json.html', locals())

def about(request):
    return render(request, 'about_basic.html', locals())