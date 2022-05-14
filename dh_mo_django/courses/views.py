from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def index(request):
    return render(request, "index.html", context={
        'name': "Manh Cuong"
    })
    
    

def welcome(request, year:int):
    return HttpResponse(f"HELLO - {year}")

def welcome2(request, year:int):
    return HttpResponse(f"HELLO-2 - {year}")


class TestView(View):
    def get(self, request):
        return HttpResponse("Welcome testing")
    
    def post(self, request):
        pass