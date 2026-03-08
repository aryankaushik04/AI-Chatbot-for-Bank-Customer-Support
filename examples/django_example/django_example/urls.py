"""
URL configuration for django_example project.
"""
from django.contrib import admin
from django.urls import path
from django_example.views import ChatSupportAppView, ChatSupportApiView


urlpatterns = [
    path('', ChatSupportAppView.as_view(), name='main'),
    path('api/chat-support/', ChatSupportApiView.as_view(), name='chat_support'),
    path('admin/', admin.site.urls, name='admin'),
]
