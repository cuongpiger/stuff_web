from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


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
    
    def __str__(self):
        return self.subject
    
    
    
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
        
    content = RichTextField()
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE) # vì thuộc tính này tham chiếu đến course nên class course có thể truy vấn đến các thuộc tính của lesson qua lesson_set, ngoài ra do chỉ đĩnh related_name rồi nên sài related name thay vì lesson_set
    tags = models.ManyToManyField('Tag', related_name="lessons", blank=True, null=True)
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    


# vidu trong bảng user có mối quan hệ OneToOne (dùng để mở rộng một bảng ra), nhớ dùng primary_key=True để không tạo ra khóa chính ở bảng con
# user_extend = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


"""

"""