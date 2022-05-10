from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    avater = models.ImageField(upload_to='uploads/%Y/%m')


class Category(models.Model): # under data will be courses_category
    name = models.CharField(null=False, unique=True, max_length=100)
    
    def __str__(self):
        return self.name
    
class ItemBase(models.Model):
    class Meta:
        abstract = True
        
    subject = models.CharField(null=False, max_length=100)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    
    
class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category') 
        ordering = ["-id"]
        
    description = models.TextField(null=False, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    
class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')
        # db_table = '...' # dùng tên này thay cho tên mặc định tạo ra trong database
        # app_label = "..."
        
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)