from django.contrib import admin
from django.db.models import fields
from django.utils.html import mark_safe
from django import forms
from .models import Category, Lesson, Course, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget


"""
Cái này dùng làm cho form
"""
class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model = Lesson
        fields = '__all__'
        
        
class LessonTagInline(admin.TabularInline):
    # StackedInline
    model = Lesson.tags.through
    


"""
này custom lại trang admin của Lesson
"""
class LessonAdmin(admin.ModelAdmin):
    
    class Media:
        css = {
            'all': ('/static/css/main.css',)
        }
        
        # js = ('/static/js/main.js',)
    
    form = LessonForm
    list_display = ['id', 'subject', 'created_date', 'active', 'course'] # these fields will be displayed on the admin page
    search_fields = ['subject', 'created_date', 'course__subject'] # course__subject là đi đến khóa ngoại tìm kiếm luôn
    list_filter = ['subject', 'course__subject']

    readonly_fields = ['avatar'] # các trường chỉ cho phép đọc
    
    inlines = (LessonTagInline,)
    
    
    def avatar(self, lesson):
        """
        hiển thị ảnh trên admin page
        """
        return mark_safe('<img src="/static/{img_url}" alt="{alt}" width="120px" />'.format(img_url=lesson.image.url, alt=lesson.subject))


class LessonInline(admin.StackedInline):
    model = Lesson
    pk_name = 'course' # khóa ngoại trỏ đến Course object của Lesson
    
    

    
"""
Từ đây có thể thêm ngay bài học ngay trang page của Course
"""
class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInline,)


# Register your models here.
admin.site.register(Category)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)

