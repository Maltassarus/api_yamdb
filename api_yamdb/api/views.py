from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User

from .serializers import SignUpSerializer, TokenSerializer


class SignUpViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()

    def create(self, request):
        # t = User.objects.filter(**request.data).exists()
        if User.objects.filter(**request.data).exists():
            user = get_object_or_404(User, username=request.data['username'])
            self.send_confirmation_code(user)
            return Response(
                {
                    'email': request.data['email'],
                    'username': request.data['username'],
                },
                status=status.HTTP_200_OK,
            )
        response = super().create(request)
        user = get_object_or_404(User, username=response.data['username'])
        self.send_confirmation_code(user)
        response.status_code = status.HTTP_200_OK
        return response

    def send_confirmation_code(self, user):
        subject = 'Confirmation of registration'
        code = default_token_generator.make_token(user)
        message = f'confirmation_code : "{code}"'
        from_email = 'api@yamdb.ru'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)


@api_view(['POST'])
def token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username'],
    )

    if not default_token_generator.check_token(
        user,
        serializer.validated_data['confirmation_code']
    ):
        error_message = 'Неверный confirmation_code'
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    jwt = AccessToken.for_user(user)
    return Response({'token': str(jwt)}, status=status.HTTP_200_OK)
