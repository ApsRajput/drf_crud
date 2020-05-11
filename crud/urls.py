from django.urls import include, path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name="hello_world")
]
