from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('', views.log_out, name='log_out'),
    path('user/logged_in/home', views.home, name='home'),
    path('user/logged_in/table', views.table, name='table'),
    path('user/logged_in/charts', views.charts, name='charts'),
]