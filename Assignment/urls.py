"""
URL configuration for Assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Question_one.views import create_user_view
from Question_two.views import create_new_user_view
from Question_three.views import create_again_user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user/', create_user_view, name='create_user'),
    path('create-new-user/', create_new_user_view, name='create_new_user'),
    path('create-again-user/', create_again_user_view, name='create_again_user'),
]
