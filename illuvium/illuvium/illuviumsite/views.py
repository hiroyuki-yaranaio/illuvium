
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def activity(request):
    context = {}
    return render(request,"illuviumsite/activity.html",context)

def augments(request):
    context = {}
    return render(request,"illuviumsite/augments.html",context)

def patchnote(request):
    context = {}
    return render(request,"illuviumsite/patchnote.html",context)

def resources(request):
    context = {}
    return render(request,"illuviumsite/resources.html",context)
