# coding:utf-8
from django import VERSION
from .widgets import UEditorWidget, AdminUEditorWidget
from .views import get_ueditor_controller
from django.conf.urls import  path

urlpatterns = [
    url('controller/', get_ueditor_controller),
]
