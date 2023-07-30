from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from quick_publisher.celery import app
from publish.models import Post

from django.conf import settings
import logging


REPORT_TEMPLATE = """

Here's how you did till now:
{% for post in posts %}
"{{ post.title }}": viewed {{ post.view_count }} times |
{% endfor %}

"""

@app.task
def send_view_count_report():
    for user in get_user_model().objects.all():
        posts = Post.objects.filter(author=user)
        if not posts:
            continue
        template = Template(REPORT_TEMPLATE)
        #user = UserModel.objects.get(pk=user_id)
        subject='Your QuickPublisher Activity'
        message = template.render(context=Context({'posts': posts}))
        email_from = settings.EMAIL_HOST_USER,
        email=[user.email],
        logging.info(message)
        send_mail(subject, message, email_from, [email], fail_silently=True)
  

