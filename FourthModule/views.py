from django.http import HttpResponse
from django.shortcuts import render

def fourthHome(request):
    return HttpResponse("WELCOME TO THE HOME PAGE")

def addtask(request):
    return HttpResponse("ADD TASK")

