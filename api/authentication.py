from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomToken

class CustomTokenAuthentication(BaseAuthentication):
  def authenticate(self, request):
    token_key = request.headers.get("token")

    if not token_key:
      return None
    try:
      token = CustomToken.objects.get(key=token_key)
    except CustomToken.DoesNotExist:
      raise AuthenticationFailed('Invalid token.')
    
    return (token.user, token)