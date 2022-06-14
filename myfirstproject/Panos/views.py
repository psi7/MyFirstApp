from django.http import HttpResponse
from django.shortcuts import render
from django import  *
# Create your views here.


def index(request):
    return HttpResponse("Welcome Panos!!!")