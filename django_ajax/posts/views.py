from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list_and_created(request):
    qs = Post.objects.all() # get all posts in the database
    return render(request, 'posts/main.html', {
        'qs': qs
    })