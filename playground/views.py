from django.shortcuts import render
from django.http import HttpResponse

# views in django is equal to Request response handler
def say_hello(request):      
    return render(request,'hello.html',{'name': 'Mushtaq'})
