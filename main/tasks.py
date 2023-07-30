import logging
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from quick_publisher.celery import app

from django.conf import settings
import logging

@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        subject='Verify your QuickPublisher account'
        #message= P'Follow this link to verify your account: ''http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(instance.verification_uuid)}),
        message =  'Follow this link to verify your account: http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
        email_from = settings.EMAIL_HOST_USER,
        email=[user.email]
        logging.info(message)
        send_mail(subject, message, email_from, [email], fail_silently=False)
  
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
