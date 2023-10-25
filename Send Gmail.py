# ===========================================================
# Activate Gmail account for email senders


# The email account used to send emails must have 2-step verification

# Go to the following address to get the password for sending email:
#       Gmail Acount > Manage your Google Account > Security > 2-step verification > App passwords

# Create a new app

# Get your 16-digit password


# ===========================================================
# settings


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''    # Sender's email
EMAIL_HOST_PASSWORD = ''    # The password created for the sender's email


# ===========================================================
# utils Package
# email_server.py


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, context, template_name):
    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)


# ===========================================================
# views.py


send_email("Email Subject", 'Email recipient', {context}, "template_path")


# ===========================================================
# Description

# First, you need to create a function that will handle the process of sending the email. (send_email)
# In this function, you send the subject, recipient email, context, and template name.

# The context value is combined with the html-css template and sent in the body of the email.