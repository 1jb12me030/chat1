from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.chat_screen, name='chat_screen'),
    path('fetch_chat_history/', views.fetch_chat_history, name='fetch_chat_history'),
    path('send_message/', views.send_message, name='send_message'),
    
]
