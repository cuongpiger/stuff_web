from django.urls import path
from .views import IndexClass, LoginClass

urlpatterns = [
    path('', IndexClass.as_view(), name='index'),
    path('login/', LoginClass.as_view(), name='login')
]
