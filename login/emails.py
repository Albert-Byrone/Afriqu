from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_credentials(password,receiver):
    subject = 'Taste Afrique Password Management.'
    sender = 'albertbyrone1677@gmail.com'

    # text_content = render_to_string('email/passwordemail.txt', {"password":password})
    html_content = render_to_string('email/passwordemail.html', {"password":password})

    send_mail(subject,html_content,sender,[receiver])
    # msg.attach_alternative(html_content, 'text/html')
    # import pdb; pdb.set_trace()
    # msg.send()
    # print(msg.send())
