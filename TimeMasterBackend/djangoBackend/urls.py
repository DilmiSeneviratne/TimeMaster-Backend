"""
URL configuration for djangoBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.urls import re_path as url
from TimeMaster import views, userView
import knox.views
# from  .views import RegisterAPI,LoginAPI
from knox import views as knox_views

urlpatterns = [
    url(r'^student$',views.studentApi),
    url(r'^student$',views.studentApi),
    url(r'^student/([0-9]+)$',views.studentApi),
    re_path(r'^task$',views.taskApi),
    re_path(r'^task/([a-zA-Z0-9]+)$',views.taskApi),
    path('home',views.Home_view),
    path('admin/', admin.site.urls),
    # path('', include('accounts.urls')),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/',knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/',knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('check/', views.check_user, name='check token'),
    path('user/',userView.userViewSet.as_view()),
    path('admin/', admin.site.urls),
]