# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import transaction

def create_again_user_view(request):
    try:
        with transaction.atomic():
            # Create a new user
            user = User.objects.create(username='testuser')
            # Intentionally raise an exception to roll back the transaction
            raise Exception("Forcing a rollback")
    except Exception as e:
        print(f"Error occurred: {e}")
        return HttpResponse("Transaction rolled back due to an error.")
    
    return HttpResponse(f"User {user.username} has been created!")
