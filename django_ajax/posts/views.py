from django.http import JsonResponse
from django.shortcuts import render
from .models import Post
from django.core import serializers

# Create your views here.
def post_list_and_created(request):
    qs = Post.objects.all() # get all posts in the database
    return render(request, 'posts/main.html', {
        'qs': qs
    })
    
    
def load_post_data_view(request, num_posts):
    visible = 3
    upper = num_posts
    lower = upper - visible 
    size = Post.objects.all().count()
    qs = Post.objects.all()
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'body': obj.body,
            'liked': True if request.user in obj.liked.all() else False,
            'count': obj.like_count,
            'author': obj.author.user.username   
        }
        data.append(item)
        
    return JsonResponse({'data': data[lower:upper], 'size': size})
    
def like_unlike_post(request):
    if request.is_ajax():
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        
        if request.user in obj.liked.all(): # if this user liked this post before, remove him from the list
            liked = False
            obj.liked.remove(request.user)
        else: # if this is the fist time this user like this port, add him to the list
            liked = True
            obj.liked.add(request.user)
            
        return JsonResponse({'liked': liked, 'count': obj.like_count})
        
    
def hello_world_view(request):
    return JsonResponse({
        'text': 'Manh Cuong is too cool, handsome'
    })