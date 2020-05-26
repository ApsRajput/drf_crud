from rest_framework import serializers
from . import models

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = ('id', 'name')

class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ('id', 'name')

class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = ('id', 'name', 'what', 'to_who', 'when', 'returned')

class Student_ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student_Class
        fields = ['id', 'room_number', 'time_table', 'course']

class FacultySerializer(serializers.ModelSerializer):
    student_class = Student_ClassSerializer(many=True, read_only=True)

    class Meta:
        model = models.Faculty
        fields = ['id', 'user', 'fname', 'lname', 'gender', 'address', 'city', 'state', 'nationalism', 'email', 'mobile', 'student_class']
