from django.shortcuts import render
from .models import Message, Group
# Create your views here.


def index(request, name):
    group = Group.objects.filter(name=name).first()
    messages = []
    if group:
        messages = Message.objects.filter(group__name=name)
    else:
        group = Group(name=name)
        group.save()
    return render(request, 'index.html', {"name":name, "messages":messages})