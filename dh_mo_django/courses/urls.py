from django.urls import path, re_path
from . import views
from .admin import admin_site

urlpatterns = [
    path('', views.index, name='index'),
    path("admin/", admin_site.urls),
    path('welcome/<int:year>/', views.welcome, name='welcome'),
    re_path(r'^welcome2/(?P<year>[0-9]{1,2})/$', views.welcome2, name='welcome2'), # take from 1 to 2 digits, lấy đúng 4 kí tự thì thay {1,2} thành {4}
    path('test/', views.TestView.as_view(), name='test'),
] 