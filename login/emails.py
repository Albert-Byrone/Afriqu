from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_credentials(password,name,receiver):
    subject = 'Taste Afrique PAssword Management.'
    sender = 'albertbyrone1677@gmail.com'

    text_content = render_to_string('email/passwordemail.txt', {"password":password, "name":name})
    html_content = render_to_string('email/passwordemail.html', {"password":password, "name":name})

    msg = EmailMultiAlternatives((subject,text_content,sender))
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
