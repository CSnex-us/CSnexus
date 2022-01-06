import re
from django.utils.timezone import datetime
from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, CSNexus!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )