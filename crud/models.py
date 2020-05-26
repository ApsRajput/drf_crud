from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.conf import settings

class OwnedModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Belonging(OwnedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Borrowed(models.Model):
    name = models.CharField(max_length=50)
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

Gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)
Exam_type = (
    ("Half Yearly", "Half Yearly"),
    ("Quarter", "Quarter"),
    ("Final", "Final"),
)

class User(AbstractUser):
    is_teacher = models.BooleanField(null=True, blank=True)
    is_student = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.username

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    joining_date = models.DateTimeField(default=datetime.datetime.now)
    mobile = models.CharField(max_length=10)

class Student_Class(models.Model):
    room_number = models.CharField(max_length=5)
    time_table = models.CharField(max_length=50)
    course = models.CharField(max_length=20, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='student_class')

    def __str__(self):
        return self.room_number

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     fname = models.CharField(max_length=30)
#     lname = models.CharField(max_length=30)
#     gender = models.CharField(max_length=20,choices=Gender)
#     Address = models.CharField(max_length=100)
#     city = models.CharField(max_length=30)
#     state = models.CharField(max_length=30)
#     nationalism = models.CharField(max_length=30)
#     email = models.EmailField(max_length=254)
#     stu_class = models.ForeignKey(Student_Class, on_delete=models.CASCADE)
#     joining_date = models.DateField(auto_now=True)
#     mobile = models.CharField(max_length=10)
#     father_name = models.CharField(max_length=50)
#     mother_name = models.CharField(max_length=50)
#     parents_contact = models.CharField(max_length=30)