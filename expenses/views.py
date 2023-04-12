from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
# Create your views here.

def home(request):
    return render(request, 'home_page.html')   
def exp_page(request):
    expenses = Expense.objects.all()
    context = {
        'expenses': expenses
    }
    return render(request, 'expenses_page.html', context)

def add(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exp_page')
    form = ExpenseForm()
    context = {
        'form': form
    }
    return render(request, 'add_expenses.html', context)   

def update(request, expense_id):
    expense = get_object_or_404(Expense, id = expense_id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance = expense)
        if form.is_valid():
            form.save()
            return redirect('exp_page')
    
    form = ExpenseForm(instance=expense)
    context = {
        'form': form
    }
    return render(request, 'update_expenses.html', context)

def delete(request, expense_id): 
    expense = get_object_or_404(Expense, id = expense_id)
    expense.delete()
    return redirect('exp_page')



