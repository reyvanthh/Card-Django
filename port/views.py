from django.shortcuts import render
from django.http import HttpResponse
from.models import Profile2


def home(request):
    product=Profile2.objects.all()
    return render(request,'card.html',{"product":product})
