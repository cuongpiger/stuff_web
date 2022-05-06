from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # auto generate form components which match to all fields in the model 
        exclude = ['host', 'participants'] # exclude some fields
        

class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email']