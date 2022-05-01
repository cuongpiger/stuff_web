from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
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
    
    
class ViewUser(LoginRequiredMixin, View): # only user who is logged in can access these views in this class
    login_url = '/login/' # user will be redirected to this url if he/she is not logged in
    def get(self, request):
            return HttpResponse("<h1>This is user view</h1>")
        
    def post(self, request):
        pass
        
        
# if user go to this url without login, it will redirect to login page
@decorators.login_required(login_url='/login/')
def view_product(request):
    # only valid user can access this url
    return HttpResponse("View product")