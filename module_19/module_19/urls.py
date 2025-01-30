from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from task1.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('platform/', platform),
    path('platform/games', games),
    path('platform/cart', cart),
    path('login/django', sign_up_by_django),
]
