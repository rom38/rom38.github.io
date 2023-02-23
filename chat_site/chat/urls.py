# chat/urls.py
from django.urls import path

from .views import index, room, register_request


urlpatterns = [
    path("", index, name="chat_index"),
    path("<str:room_name>/", room, name="room"),
    # path("register/", register_request, name="register"),


]
