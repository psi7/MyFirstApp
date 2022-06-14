from django.contrib import admin
from django.urls import path, include
from tasks import views
app_name='tasks'#specific url to tasks
urlpatterns = [
    path('',views.index,name='index')
    ,path('add',views.addTask, name='add')
]
