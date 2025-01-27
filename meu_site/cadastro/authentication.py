from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

# Personalisando a função authenticate para ser possivel fazer login com email
class AuthenticationEmail(ModelBackend):

    def authenticate(self, request, username = None, password = None):
        
        try:
            user = User.objects.get(email = username)
        
        except User.DoesNotExist :
            return None
        
        if user.check_password(password):
            return user
        
        return None