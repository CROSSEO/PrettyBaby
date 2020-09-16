from . import views
from PrettyBaby.views import *
from django.urls import path


app_name = 'landing_page'

urlpatterns = [
    path('', LandingPage.as_view(), name='home'),
    path('terms-and-conditions/', Terms.as_view(), name='terms'),
    path('privacy-and-policy/', Privacy.as_view(), name='privacy'),
]
