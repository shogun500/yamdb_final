from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken


def send_verification_email(data, code):
    email = data.get('email')
    username = data.get('username')
    subject = 'Код подтверждения'
    message = (
        f'Уважаемый {username}, Ваш код подтверждения для регистрации:'
        f'{code}'
    )
    from_email = 'admin@yamdb.ru'
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[email]
    )


def get_token_for_user(user):
    token = RefreshToken.for_user(user)
    return {
        'refresh': str(token),
        'access': str(token.access_token)
    }
