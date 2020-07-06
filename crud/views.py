from .permissions import IsOwner
from rest_framework import viewsets, permissions
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

@api_view(["GET", "POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"message": "Hello World!"})

    else:
        name = request.data.get("name")
        if not name:
            return Response({"error": "No name passed"})
        return Response({"message": "Hello {}!".format(name)})

#  ModelViewsets
class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer
    permission_classes = [permissions.IsAuthenticated]

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST'])
def FriendFunction(request):
    if request.method == 'GET':
        data = models.Friend.objects.all()

        serializer = serializers.FriendSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.FriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Generics
class FriendGenericslc(generics.ListCreateAPIView):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

class FriendGenericsrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

class Teachers(generics.ListCreateAPIView):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer
    # permission_classes = [permissions.IsAuthenticated]

class Class(generics.ListCreateAPIView):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.Student_ClassSerializer
    # permission_classes = [permissions.IsAuthenticated]