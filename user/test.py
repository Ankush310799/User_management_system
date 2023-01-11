import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usermanagementsystem.settings')
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from user.models import User
import unittest

if __name__ == '__main__':
    unittest.main()

class RegistrationAPIViewTests(APITestCase):
    """
    Test_cases_ for_registration 
    """
    registration_url = reverse('user:register')
    def test_post_register(self):

        data = {

            "first_name": "Ankush",
            "last_name": "Pomendkar",
            "date_of_birth": "1999-02-12",
            "username": "Ankush@",
            "password": "Ankush@",
            "email": "ankushpomendkar5@gmail.com",
            "phone": "9878986545",
            "street": "sainath nagar",
            "zip_code": 415607,
            "city": "pune",
            "state": "Maharashtra",
            "country": "India"

        }
        response = self.client.post(self.registration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  

class UserViewTests(APITestCase):
    """
    #Test_cases_for_Accessing Userdetails
    """
    def setUp(self):
        self.url = reverse('user:login')

    def test_get_user(self):
        self.user=User.objects.create_user(
            username='ankush22@', email='ankushpomendkar22@gmail.com', password='ankush22@')
        self.client.login(username='ankush22@', password='ankush22@')
        response = self.client.get(reverse('api:user_detail',args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            
    def test_update_user(self):
        self.user=User.objects.create_user(
            username='ankush12@', email='ankushpomendkar12@gmail.com', password='ankush12@')
        self.client.login(username='ankush12@', password='ankush12@')
        data= {
                "phone": "8976040545",
                }
        response = self.client.response = self.client.patch(reverse('api:user_detail', args=[self.user.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
          
    def test_delete_user(self):
        self.user = User.objects.create_user(
            username='ankush32@', email='ankushpomendkar32@gmail.com', password='ankush32@')
        self.client.login(username= 'ankush32@', password='ankush32@')
        response = self.client.delete(reverse('api:user_detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 
class LoginAPIViewTest(APITestCase):
    """
    #Possible valid or invalid user-login test cases 
    """
    def setUp(self):
        self.url = reverse('user:login')

    def test_login(self):
        self.url = reverse('user:login')
        user = User.objects.create_user(
            username='ankush@',  password='ankush@')
        user.is_active = True
        resp = self.client.post(
            self.url, {'username': 'ankush@', 'password': 'ankush@'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
    
    def test_login_no_password(self):
        self.url = reverse('user:login')
        data = {
            "username": "Ankush@",
            "password": " ",
            }
        response = self.client.post(self.url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login_no_username(self):

        self.url = reverse('user:login')
        data = {
            "username": " ",
            "password": "Ankush@",
            }
        response = self.client.post(self.url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login_invalid_crediantial(self):

        self.url = reverse('user:login')
        data = {
            "username": "Ankush123@",
            "password": "Ankush23@",
            }
        response = self.client.post(self.url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
 
class LogoutAPIViewTest(APITestCase):
    """
    Logout API Test Cases 
    """
    def setUp(self):
        self.url = reverse('user:logout')
  
    def test_logout_for_Autherized_user(self):
        user = User.objects.create_user(
            username='Ankush@', password='Ankush@')
        self.client.force_authenticate(user=user)
        self.url = reverse('user:logout')
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
  