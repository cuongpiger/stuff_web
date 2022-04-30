from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name='detail'),
    path('list/', views.viewlist, name='view_list'),
    path('', views.index, name='index'),
    path('<int:question_id>', views.vote, name='vote'),
]
