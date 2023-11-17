from django.urls import path
from . import views

urlpatterns = [
    path('api/user/get_menu' , views.get_items),
    path('api/user/make_order',views.do_order , name = 'do_order')
]