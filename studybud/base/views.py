from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Message, Room, Topic
from .forms import RoomForm

# rooms = [
#     {'id': 1, 'name': 'Lets learn Python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]

def loginPage(request):
    page = 'login'
    
    # if the user is already logged in, redirect to home
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
    
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist!')
    
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # get data from form
        
        if form.is_valid(): # check if data is valid
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'AN error occured during registration!')
        
    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' # get value from parameters of URL
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q)) # get value based on foreign key (video at 2:14:26)
    
    topics = Topic.objects.all() # get all topics
    room_count = rooms.count()
    
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


# URL has parameters
def room(request, pk):
    room:Room = Room.objects.get(id=pk) # get room by id
    room_messages = room.message_set.all().order_by('-created') # get all messages from room with order by created
    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
    
        room.participants.add(request.user)
        
        return redirect('room', pk=room.id) # redirect to same page
    
    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def createRoom(request):
    """
    User ought to be logged in to create a room
    """
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid(): # if data is valid
            form.save()
            return redirect('home') # redirect to home page
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) # fill in the form with the data of the room
   
    # if user try to edit the room that is not his own
    if request.user != room.host:
        return HttpResponse('You are not allowed to edit this room!')
        
   
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) # replace the data of the room with the data in the form (POST data)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    # if user try to edit the room that is not his own
    if request.user != room.host:
        return HttpResponse('You are not allowed to delete this room!')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    # if user try to edit the room that is not his own
    if request.user != message.user:
        return HttpResponse('You are not allowed to delete this room!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': message})