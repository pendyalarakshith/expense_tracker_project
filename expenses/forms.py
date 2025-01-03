from django import forms
from .models import Expense,Category

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date', 'description']

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")
