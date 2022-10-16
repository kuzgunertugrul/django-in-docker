from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pentestivirzivir/login', views.login_page, name='login'),
    path('pentestivirzivir/logout', views.logout_user, name='logout'),
    path('pentestivirzivir/',views.pentestivirzivirView, name='pentestivirzivir')
]