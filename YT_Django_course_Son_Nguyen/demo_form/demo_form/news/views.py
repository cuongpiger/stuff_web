from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail

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
    
    
def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})


def process(request):
    if request.method == 'POST':
        m = SendEmail(request.POST)
        
        if m.is_valid():
            tieude = m.cleaned_data.get('title')
            cc = m.cleaned_data.get('cc')
            noidung = m.cleaned_data.get('content')
            email = m.cleaned_data.get('email')
            
            context = {'td': tieude, 'c': cc, 
                       'b': noidung, 'd': email}
            
            context2 = {'email_data': m}
            
            # return render(request, 'news/print_email.html', context)
            return render(request, 'news/print_email.html', context2)
        
        else:
            return HttpResponse("Form not validate!")
    else:
        return HttpResponse("This is not a POST method!")