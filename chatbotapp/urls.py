from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),  
    path("chatbot/", views.index, name="chatbot"),  
    path("chatbot/response/", views.chatbot_response, name="chatbot_response"),
]
