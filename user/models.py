from django.db import models
from django.contrib.auth.models import  AbstractUser
import os
from django.conf import settings
from django.db.models.signals import post_save  
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
os.environ.setdefault('DJANGO_SETTINGS_MODULE','usermanagementsystem.settings')

# Create your models here.
class User(AbstractUser):
    """
    By using AbstractUser,here extend user module with costum fields.  
    """
    date_of_birth=models.DateField(null=True)
    email=models.EmailField(max_length=250,unique=True)
    phone=models.CharField(max_length=10,unique=False)
    street=models.CharField(max_length=500)
    zip_code=models.IntegerField(null=True)
    city=models.TextField(max_length=400)
    state=models.TextField(max_length=400)
    country=models.TextField(max_length=400)
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Created Token for user
    """
    if created:
        Token.objects.create(user=instance)
        