from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<service_user>/Services/<category>', views.category, name='category')
]