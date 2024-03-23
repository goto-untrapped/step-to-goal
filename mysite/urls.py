"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from myapp.views import CsrfView, PingView, loginView, myTargetView, registerView, targetView, userSaveView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myapp/", include('myapp.urls')),
    path('csrf/', CsrfView),
    path('ping/', PingView),
    path('api/target', targetView),
    path('api/save/', registerView),
    path('api/user/save', userSaveView),
    path('api/login', loginView),
    path('api/target/mytarget', myTargetView),
]
