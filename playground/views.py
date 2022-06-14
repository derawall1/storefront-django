
from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
    #   message = EmailMessage('subject', 'message','from@codesnipers.com',['derawall@gmail.com'])
    #   message.attach_file('playground/static/images/dog.jpg')
    #   message.send()
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Muhammad Mushtaq'}
        )
        #message.to = ['info@codesnipers.com']
        message.send(['info@codesnipers.com'])
    except BadHeaderError:
        pass
    return render(request,'hello.html',{'name': 'Mushtaq'})#, 'result': list(query_set)})
