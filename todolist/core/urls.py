
from django.urls import path

from . import views


urlpatterns = [
    path('signup', views.RegistrationVeiw.as_view(), name='signup'),
    path('login', views.LoginVeiw.as_view(), name='login'),
]
