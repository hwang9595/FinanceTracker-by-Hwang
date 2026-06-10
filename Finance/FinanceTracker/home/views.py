from django.shortcuts import render
from django.db.models import Sum
from decimal import Decimal

from goals.models import Goal
from transactions.models import Transaction

def home(request):
    income = Transaction.objects.filter(type=Transaction.INCOME).aggregate(
        total=Sum('amount')
    )['total'] or Decimal('0.00')
    expenses = Transaction.objects.filter(type=Transaction.EXPENSE).aggregate(
        total=Sum('amount')
    )['total'] or Decimal('0.00')
    balance = income - expenses
    latest_transactions = Transaction.objects.select_related('category')[:5]
    active_goals = Goal.objects.all()[:3]

    return render(
        request,
        'home.html',
        {
            'income': income,
            'expenses': expenses,
            'balance': balance,
            'latest_transactions': latest_transactions,
            'active_goals': active_goals,
        }
    )
