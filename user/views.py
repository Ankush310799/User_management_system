"""
Viewsets allow us to define functions that match to common API object actions like : 
LIST, CREATE, RETRIEVE, UPDATE, etc.
"""
from .serializers import RegisterSerializer,LoginSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .utils import Util,token_generator
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import status
from rest_framework import viewsets
from .permissions import Userpermission, UserListPermission
from django_filters.rest_framework import DjangoFilterBackend,filters
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token 
from django.contrib.auth import logout
from rest_auth.views import LoginView,LogoutView

class UserRegisterView(generics.GenericAPIView):
    """
    Registration View for user.
    """
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_active=False)

        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token, _ = Token.objects.get_or_create(user=user)
        current_site = get_current_site(request).domain
        uidb64= urlsafe_base64_encode(force_bytes(user.pk))
        relativeLink = reverse('user:verify',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
        absurl = 'http://'+current_site+relativeLink
        email_body = 'Hi'+" "+ user.username + \
            'Use below link to verify your account\n' + absurl
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': 'Verify your Registration'
        }
        Util.send_email(data)
        return Response({"Message ": "Check your given Email-id"}, status=status.HTTP_201_CREATED,)

class Verify_Registration(generics.GenericAPIView):
    """
    Here,Verify User Registration by sending E-mail on register Email-Id
    """
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        
            user.is_active = True
            user.save()
            return Response({'Message ':'Account Activated Successfully !'})
                    
        except (TypeError, ValueError, OverflowError, User().DoesNotExist):
            return Response({'Message':'Invalid Token'})

class UsersListView(viewsets.ModelViewSet):
    """
    Only Super-User can access this Data
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (UserListPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'username', 'email']
    search_fields = ['first_name', 'last_name']
    lookup_url_kwarg = 'pk'

    def get_object(self):
        obj = get_object_or_404(User.objects.filter(id=self.kwargs["pk"]))
        self.check_object_permissions(self.request, obj)
        return obj

class UserDetails(viewsets.ModelViewSet):
    """
    User can get only it's own details and super user can handle all user details.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (Userpermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'username', 'email']
    search_fields = ['first_name', 'last_name']
    kwarg = 'id'

    def get_queryset(self):
        user = self.request.user.id
        return User.objects.filter(id=user)

class Login(LoginView):
    """
    Login with valid crediential for accessing data
    """
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    
class Logout(LogoutView):
    """
    Delete Token of existing logged user.
    """
    def post(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response({"Success":"Token deleted successfully !"},status=status.HTTP_200_OK)
