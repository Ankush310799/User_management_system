from django.apps import AppConfig
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','usermanagementsystem.settings')

class UserConfig(AppConfig):
    """
    Register apps -
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
