from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
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
        
        if my_user is None: # if this user does not exist
            return HttpResponse("This user does not exist")
        
        
        # this user exists on database
        login(request, my_user) # login with this user
        return render(request, 'Login/thanhcong.html')
    
    
class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse("You are not login")
        else:
            return HttpResponse("<h1>This is user view</h1>")