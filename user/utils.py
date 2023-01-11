from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class Util:
    """
    To send Verification E-mail to user
    Static method used to send-email
    """  
    @staticmethod
    def send_email(data):
        email=EmailMessage(
            subject=data['email_subject'],body=data['email_body'],to=[data['to_email']],)
        
        """ Send email to user """      
        return email.send()

class AppTokenGenerator(PasswordResetTokenGenerator):
    """
    To make data in hashable value
    """
    def __make_hash_value(self,user,timestamp):
        return (text_type(user.is_active)+text_type(user.pk)+text_type(timestamp))

token_generator=AppTokenGenerator()
