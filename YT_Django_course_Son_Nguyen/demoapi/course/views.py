from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerializer, CourseSerializer

# Create your views here.
class GetAllCoursesAPIView(APIView):
    def get(self, request):
        list_courses = Course.objects.all()
        mydata = GetAllCourseSerializer(list_courses, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

    def post(self, request):
        mydata = CourseSerializer(data=request.data)
        
        if not mydata.is_valid():
            return Response("Your data format is not correct!", status=status.HTTP_400_BAD_REQUEST)
        
        title = mydata.data.get('title')
        content = mydata.data.get('content')
        price = mydata.data.get('price')
        cs = Course.objects.create(title=title, price=price, content=content)
        
        return Response(data=cs.id, status=status.HTTP_200_OK)