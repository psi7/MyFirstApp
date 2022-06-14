from django.http import HttpResponse
from django.shortcuts import render
from django import *
import datetime
# Create your views here.


def index(request):
    return HttpResponse("Hello World")

def daytime(day):
    return datetime.datetime