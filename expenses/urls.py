from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('expenses/', views.exp_page, name="exp_page"),
    path('add/', views.add, name="add"),
    path('update/<expense_id>', views.update, name="update"),
    path('delete/<expense_id>', views.delete, name="delete"),

   
]