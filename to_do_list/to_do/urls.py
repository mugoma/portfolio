"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView,redirect_to_login
from django.urls import path
from . import views


app_name="to_do"

urlpatterns = [
    path("login/",LoginView.as_view(),name="login"),
    path("login/redirect/",redirect_to_login,name="login_redirect"),
    

    path("add/", views.CreateTaskView.as_view(), name="create_view"),
    path("add/function/", views.create_task_view, name="create_function"),
    path("list/<str:username>",views.ListTasksView.as_view(),name="list_view"),
    path("<int:pk>/", views.DetailTaskView.as_view(), name="detail_view"),
]
