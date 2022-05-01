from django.urls import path
from .views import IndexClass

urlpatterns = [
    path('', IndexClass.as_view(), name='index'),
]
