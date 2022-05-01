from django.urls import path
from .views import AddPost, IndexClass, LoginClass, ViewUser, view_product

app_name = 'Login'
urlpatterns = [
    path('', IndexClass.as_view(), name='index'),
    path('login/', LoginClass.as_view(), name='login'),
    path('user-view/', ViewUser.as_view(), name='user_view'),
    path('view-pro/', view_product, name='view-product'),
    path('add-post', AddPost.as_view(), name='add_post')
]
