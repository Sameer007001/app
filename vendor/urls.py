from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.index, name='vendor_sign_up'),
    path('addVendor', views.insertVendor, name='insertVendor'),
]