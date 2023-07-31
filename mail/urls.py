from django.urls import path
from .views import (
    Home,
    SendMail,
    SendMassMail
)

urlpatterns = [
    path('', Home.as_view(), name='homepage_url'),
    path('mail', SendMail.as_view(), name='send_mail_url'),
    path('mass-mail', SendMassMail.as_view(), name='send_mass_mail_url'),
]
