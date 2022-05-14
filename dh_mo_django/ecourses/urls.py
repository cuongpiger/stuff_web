from django.contrib import admin
# from courses.admin import admin_site
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', admin_site.urls),
    path('', include('courses.urls')),
    
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
