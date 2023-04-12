from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('expenses/', views.exp_page, name="expenses"),
    path('add/', views.add, name="add"),
    path('update/', views.update, name="update"),
]