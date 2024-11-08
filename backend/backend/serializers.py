from rest_framework import serializers
from backend.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['user_id', 'is_active', 'is_staff', 'created_at', 'updated_at', "last_login", "is_superuser", "groups", "user_permissions"]
    
    def create(self, validated_data):
        # Использовать метод create_user, который мы
        # написали ранее, для создания нового пользователя.
        return User.objects.create_user(**validated_data)

class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['email','username', 'password']

class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
            # В методе validate мы убеждаемся, что текущий экземпляр
            # LoginSerializer значение valid. В случае входа пользователя в систему
            # это означает подтверждение того, что присутствуют адрес электронной
            # почты и то, что эта комбинация соответствует одному из пользователей.
            email = data.get('email', None)
            password = data.get('password', None)

            # Вызвать исключение, если не предоставлена почта.
            if email is None:
                raise serializers.ValidationError(
                    'An email address is required to log in.'
                )

            # Вызвать исключение, если не предоставлен пароль.
            if password is None:
                raise serializers.ValidationError(
                    'A password is required to log in.'
                )

            # Метод authenticate предоставляется Django и выполняет проверку, что
            # предоставленные почта и пароль соответствуют какому-то пользователю в
            # нашей базе данных. Мы передаем email как username, так как в модели
            # пользователя USERNAME_FIELD = email.
            user = authenticate(username=email, password=password)

            # Если пользователь с данными почтой/паролем не найден, то authenticate
            # вернет None. Возбудить исключение в таком случае.
            if user is None:
                raise serializers.ValidationError(
                    'A user with this email and password was not found.'
                )

            # Django предоставляет флаг is_active для модели User. Его цель
            # сообщить, был ли пользователь деактивирован или заблокирован.
            # Проверить стоит, вызвать исключение в случае True.
            if not user.is_active:
                raise serializers.ValidationError(
                    'This user has been deactivated.'
                )

            # Метод validate должен возвращать словать проверенных данных. Это
            # данные, которые передются в т.ч. в методы create и update.
            return {
                'email': user.email,
                'username': user.username,
            }