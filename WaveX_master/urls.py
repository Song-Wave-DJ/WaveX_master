"""
URL configuration for WaveX_master project.

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('api.urls')) , # testing api building site api -> urls.py -> views.py
    path('' , include('manager.urls')) ,    # all urls will get from manager -> urls.py ->views.py
    path('' , include('user.urls')) , # all urls will get from user -> urls.py ->views.py
    path('' ,include('waiter.urls')) ,  # all urls will get from waiter -> urls.py ->views.py
    path('' , include('admin.urls')) , # all urls will get from admin -> urls.py -> views.py
]
