from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    If we use the defined user model, when we access localhost:8000/admin/ and then login, the User defined model will not in the Authentication and authorization section anymore. Instead, it is in the Base section
    """
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True) # use this field for login function
    bio = models.TextField(null=True)
    
    USERNAME_FIELD = 'email' # using email for username, we need not to create a particular username field. When this field is set, we have to use email for login
    REQUIRED_FIELDS = []
    


