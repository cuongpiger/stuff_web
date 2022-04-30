from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View

# this is based class view
class IndexClass(View):
    # like def index(request):
    def get(self, request):
        ketqua = "12323345"
        return HttpResponse(ketqua)


class ClassSaveNews(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f': a})

    
    def put(self):
        pass
    
    def post(self, request):
        g = PostForm(request.POST)        
        if g.is_valid(): # match with data type we set up in Post at file news/modes.py
            g.save()
            return HttpResponse("Success!")
        else:
            return HttpResponse("Fail!")
    
    
# this is function based view
def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})


# this is function based view
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