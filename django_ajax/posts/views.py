from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list_and_created(request):
    qs = Post.objects.all() # get all posts in the database
    return render(request, 'posts/main.html', {
        'qs': qs
    })
    
    
def hello_world_view(request):
    return JsonResponse({
        'text': 'Manh Cuong is too cool'
    })