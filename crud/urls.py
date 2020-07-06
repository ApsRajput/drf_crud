from django.urls import include, path
from crud import views

urlpatterns = [
    path('', views.hello_world, name="hello_world"),
    
    #function
    path('friend', views.FriendFunction, name="friends"),

    path('friends', views.FriendGenericslc.as_view(), name="friends"),
    path('friendso/<int:pk>', views.FriendGenericsrud.as_view(), name="friendso")
]
