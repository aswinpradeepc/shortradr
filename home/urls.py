from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<str:short_code>', views.result, name='result'),
    path('<str:short_code>', views.redirect_url, name='redirect'),
]