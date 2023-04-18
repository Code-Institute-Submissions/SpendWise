from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('expenses/', views.exp_page, name="exp_page"),
    path('add/', login_required(views.add), name="add"),
    path('budget/', login_required(views.add_budget), name="budget"),
    path('update/<expense_id>', login_required(views.update), name="update"),
    path('delete/<expense_id>', login_required(views.delete), name="delete"),
    
]
 
