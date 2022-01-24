from django.shortcuts import render
from user.models import holla


def page(request):
    context = {"key" : "value", "result" : True}
    return render(request, 'login.html', context)

def index(request):
    return render(request, 'index.html')