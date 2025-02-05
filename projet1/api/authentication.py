from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from projet1.models import Token

class CustomTokenAuthentication(BaseAuthentication):
    keyword = 'Token'

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization', '').split()
        if not auth_header or auth_header[0].lower() != self.keyword.lower():
            return None

        if len(auth_header) != 2:
            raise AuthenticationFailed('Invalid token header.')

        token_key = auth_header[1]
        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        return (token.user, token)