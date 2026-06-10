from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TransactionForm
from .models import Transaction


def transaction_list(request):
    form = TransactionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Transaction added successfully!")
        return redirect('transactions')

    transactions = Transaction.objects.select_related('category').all()

    return render(
        request,
        'transaction_list.html',
        {'transactions': transactions,
         'form': form,
         }
    )


# НОВАЯ ФУНКЦИЯ: Удаление транзакции
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)

    if request.method == "POST":
        transaction_title = transaction.title
        transaction.delete()
        messages.success(request, f"Transaction '{transaction_title}' has been deleted.")
        return redirect('transactions')

    return redirect('transactions')