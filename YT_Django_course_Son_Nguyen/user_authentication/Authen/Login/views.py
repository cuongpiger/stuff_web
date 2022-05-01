from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse("<h1>Hello</h1>")


class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')
    
    def post(self, request):
        user_name = request.POST.get('tendangnhap') # get username from file login.html
        password = request.POST.get('password') # get password from file login.html
        my_user = authenticate(username=user_name, password=password) # check username and password
        
        if my_user is None:
            return HttpResponse("This user does not exist")
        return HttpResponse(f"You have logged in with {user_name} - {password}")