"""sepidlearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('index', views.index, name="index"),
    path('panel', views.panel, name="panel"),
    path('check_login', views.check_login, name="check_login"),
    path('a', views.a, name="a"),
    path('manager', views.manager, name="manager"),
    path('delete_accounts', views.delete_accounts, name="delete_accounts"),
    path('settingd', views.settingd, name="settingd"),
    path('changename', views.changename, name="changename"),
    path('change_profile', views.change_profile, name="change_profile"),
    path('panel_homework', views.panel_homework, name="panel_homework"),
    path('homework_delete', views.homework_delete, name="homework_delete"),
    path('unsafe', views.unsafe, name="unsafe")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
