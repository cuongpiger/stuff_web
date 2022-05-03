from django.db.models import fields
from rest_framework import serializers
from .models import Course

class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')
        
class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=12)
    content = serializers.CharField(max_length=12)
    price = serializers.IntegerField()