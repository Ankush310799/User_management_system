from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    """
    In admin panel ,admin user can see all records of users
    """
    List_display=("email","firstname","lastname"),
    search_field=("email","firstname","lastname"),
   
admin.site.register(User,UserAdmin)