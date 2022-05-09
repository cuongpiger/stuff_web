from django.urls import path
from .views import (
    post_list_and_created
)


app_name = 'posts'
urlpatterns = [
    path('', post_list_and_created, name='main-board'),
]
