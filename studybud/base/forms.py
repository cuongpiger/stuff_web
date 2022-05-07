from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User
# from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # auto generate form components which match to all fields in the model 
        exclude = ['host', 'participants'] # exclude some fields
        

class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['avatar', 'name', 'username', 'email', 'bio']