"""
App views connected with urls.
"""
from django.urls import path
from .views import UserRegisterView,Verify_Registration,UsersListView,Login,Logout
from . import views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns =[
    path('register/',UserRegisterView.as_view(),name='register'),
    path('verify/<uidb64>/<token>',Verify_Registration.as_view(),name='verify'),
    path('user/',views.UserDetails.as_view({'get': 'list'}),name='user'),
    path('user/<int:pk>/',views.UserDetails.as_view({'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'}),name='user_detail'),
    path('userslist/',UsersListView.as_view({'get': 'list'}),name='userslist'),
    path('userslist/<int:pk>/',UsersListView.as_view({'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'}),name='list_userdetail'),
    path('login/',Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
 
    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('user:password_reset_complete')),
        name='password_reset_confirm'),
    
    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete')
]
"""
   path('password/reset/',
        auth_views.PasswordResetView.as_view(success_url=reverse_lazy('user:password_reset_done')),
        name='reset_password'),
"""