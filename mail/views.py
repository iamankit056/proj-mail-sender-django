from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
class Home(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'mail/home.html', { 'users': users })


class SendMail(View):
    def post(self, request):
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        reciver_email = request.POST.get('reciver_email')
        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[reciver_email],
                fail_silently=False
            )
            return HttpResponse('<h4>Mail Sended Sucessesfully...</h4>')
        except:
            return HttpResponse('<h4>Failed to send mail</h4>')


class SendMassMail(View):
    def post(self, request):
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        recivers_email = User.objects.values_list('email', flat=True)
        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recivers_email,
                fail_silently=False
            )
            return HttpResponse('<h4>Mail Sended Sucessesfully...</h4>')
        except:
            return HttpResponse('<h4>Failed to send mail</h4>')