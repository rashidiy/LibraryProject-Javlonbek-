from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_email(html_template, subject, to_email, context=None):
    # Agar context None bo'lsa, bo'sh lug'atni o'rnatamiz
    if context is None:
        context = {}

    # HTML shablonni render qilish
    html_message = render_to_string(html_template, context)

    # Xabarni yaratish
    email = EmailMultiAlternatives(
        subject=subject,
        body=html_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[to_email],
    )

    # HTML alternativani qo'shish
    email.attach_alternative(html_message, "text/html")

    # Xabarni jo'natish
    email.send()
