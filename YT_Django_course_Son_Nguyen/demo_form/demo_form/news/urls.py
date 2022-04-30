from django.urls import path, include
from . import views


app_name = "news"

urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'), # based class view  
    # based function view is from here to down
    path('save/', views.ClassSaveNews.as_view(), name='save'),
    path('email/', views.email_view, name='email'),
    path('process/', views.process, name='pro'),
]
