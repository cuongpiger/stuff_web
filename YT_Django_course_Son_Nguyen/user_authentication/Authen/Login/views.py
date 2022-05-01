from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.models import User
# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse("<h1>Hello</h1>")


