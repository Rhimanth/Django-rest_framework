from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password
from .models import Users

class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        email=request.data.get('email')
        password=request.data.get('password')
        if not email or not password:
            raise AuthenticationFailed('email or password missing !!')
        try:
            user=Users.objects.get(email=email)
        except Users.DoesNotExist:
            raise AuthenticationFailed('User not found by this email !!')
        if not check_password(password,user.password):
            raise AuthenticationFailed('Invalid password !!')
        return (user,None)