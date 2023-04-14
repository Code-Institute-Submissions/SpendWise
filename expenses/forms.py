from django import forms
from .models import Expense, Budget

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'number', 'date_field']


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['max_budget']