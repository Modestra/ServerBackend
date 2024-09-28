import jwt

from django.conf import settings

from rest_framework import authentication, exceptions

from solarlabshop.models import User

class JWTAuthenrification(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        try:
            auth_header = authentication.get_authorization_header(request).decode('utf-8').split()
            auth_header_prefix = self.authentication_header_prefix.lower()

            #prefix = auth_header.decode('utf-8')
            token = auth_header[1]

        except Exception:
            raise exceptions.AuthenticationFailed("Не удалось загрузить Токен")
        
        return self._authenticate_credentials(request, token)
        
    def _authenticate_credentials(self, request, token):
        """
        Попытка аутентификации с предоставленными данными. Если успешно -
        вернуть пользователя и токен, иначе - сгенерировать исключение.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            msg = 'Ошибка аутентификации. Невозможно декодировать токеню'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'Пользователь соответствующий данному токену не найден.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'Данный пользователь деактивирован.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)