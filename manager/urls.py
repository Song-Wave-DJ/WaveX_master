from django.urls import path
from . import views

urlpatterns = [
    path('api/get_waiter' , views.getWaiter)
]