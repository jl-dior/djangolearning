# coding:utf-8
from django import VERSION
from .widgets import UEditorWidget, AdminUEditorWidget
from .views import get_ueditor_controller
from django.urls import  path

urlpatterns = [
    path('controller/', get_ueditor_controller),
]
