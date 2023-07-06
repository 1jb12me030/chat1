from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    contact_no = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    senderId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chats')
    RecId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chats')
    #recipient_id = models.IntegerField()
    #sender_id = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
