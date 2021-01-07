from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.index, name='promoter_sign_up'),
    path('addPromoter/', views.insertPromoter, name='insertPromoter'),
    path('login/', views.promoterLogin, name='promoterLogin'),

]