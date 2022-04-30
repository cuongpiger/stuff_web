from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

def index(request):
    return HttpResponse("Hello World!")


def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})


def save_news(request):
    if request.method == 'POST':
        g = PostForm(request.POST)
        
        if g.is_valid(): # match with data type we set up in Post at file news/modes.py
            g.save()
            return HttpResponse("Success!")
        else:
            return HttpResponse("Fail!")
    else:
        return HttpResponse("This is not a POST request!")
    