from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


def send_email_with_confirmation_code(request):
    email = request.data.get("email")
    confirmation_code = create_confirmation_code(request)
    send_mail(
        "System messege",
        f"confirmation_code = {confirmation_code}",
        settings.EMAIL_BACKEND_NAME,
        (email,),
        fail_silently=False,
    )


def create_confirmation_code(request):
    username = request.data.get("username")
    email = request.data.get("email")
    user = get_object_or_404(User, username=username, email=email)
    confirmation_code = default_token_generator.make_token(user)
    return confirmation_code
