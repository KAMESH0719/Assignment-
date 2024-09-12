from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import threading

def create_new_user_view(request):
    print(f"Creating user in thread: {threading.get_ident()}")
    user = User.objects.create(username='testuser')
    return HttpResponse(f"User {user.username} has been created!")
