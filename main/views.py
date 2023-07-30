from django.shortcuts import render, redirect

# Create your views here.
from django.http import Http404
from .models import MyUser
from django.conf import settings
from django.core.mail import send_mail
# Create your views here. 
 
def home(request):
    email =  'rasheedbabatunde76@gmail.com'
    subject = 'Reset Password Request:'
    message = 'Click on the link to reset your password:'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email], fail_silently=True)
    return render(request, 'home.html')
 
 
def verify(request, uuid):
    try:
        user = MyUser.objects.get(verification_uuid=uuid, is_verified=False)
    except MyUser.DoesNotExist:
        raise Http404("User does not exist or is already verified")
 
    user.is_verified = True
    user.save()
    return redirect('home')