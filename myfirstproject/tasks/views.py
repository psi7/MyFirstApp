from asyncio import constants
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from myfirstproject.utils import constants
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority",min_value=1,max_value=100)

tasks=['laundry','carfix','shopping','gardening']
def index(request):
    context={'laundry':'Panos','tasks':tasks}
    return render(request, constants.get_url_tasks(),context)

def addTask(request): 
    context={"form": NewTaskForm()}
    if request.method == "POST":
        form= NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            print(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, constants.get_url_tasks(),context)
    #
    return render(request, constants.get_url_add(), context )

