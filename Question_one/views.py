from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_user_view(request):
    # Create a new user
    user = User.objects.create(username='testuser')
    
    # Return a simple HTTP response
    return HttpResponse(f"User {user.username} has been created!")
