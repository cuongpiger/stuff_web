from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api', 
        'GET /api/rooms/',
        'GET /api/rooms/:id',
    ]
    
    # return JsonResponse(routes, safe=False) # set `safe=False` to allow API can receive dictionary data (such as JSON) and python data types
    return Response(routes) # this is valid because the data is already original data type, not a Python object data


@api_view(['GET'])
def getRooms(request):
    """
    Get multiple (all) rooms.
    """
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) # there are many objects in `rooms`, so we need to convert it to a list of JSON data, so we set `many=True`
    
    # return Response(rooms) # this occurs error because the returned data is not as type of serializable data, instead of this is a list of python object. So we need to convert the entire returned data into JSON format (or serializable data)
    return Response(serializer.data) # this is valid because the data is JSON format data, not a Python object data


@api_view(['GET'])
def getRoom(request, pk):
    """
    Get a specific room based on `id` field.
    """
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) # get a single object in Room model, so we set `many=False` 
    
    # return Response(rooms) # this occurs error because the returned data is not as type of serializable data, instead of this is a list of python object. So we need to convert the entire returned data into JSON format (or serializable data)
    return Response(serializer.data) # this is valid because the data is JSON format data, not a Python object data