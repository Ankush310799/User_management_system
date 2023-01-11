"""
Setting up urls from app,rest_framework and rest_auth
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(('user.urls',"user"),namespace='api')),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url('rest-auth/', include('rest_auth.urls'))
]
