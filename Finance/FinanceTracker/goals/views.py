from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from decimal import Decimal

from .forms import GoalForm
from .models import Goal

def goal_list(request):
    form = GoalForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('goals')
    goals = Goal.objects.all()


    return render(
        request,
        'goal_list.html',
        {'form': form,
         'goals': goals,
         }
    )


# НОВАЯ ФУНКЦИЯ: Добавление накоплений к цели
def add_savings(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)

    if request.method == "POST":
        try:
            amount = Decimal(request.POST.get('amount', '0'))

            if amount <= 0:
                messages.error(request, "Please enter a positive amount.")
                return HttpResponseRedirect(reverse('goals'))

            # Добавляем сумму к текущим накоплениям
            goal.current_amount += amount

            # Проверяем, не превысили ли мы целевой суммы
            if goal.current_amount > goal.target_amount:
                goal.current_amount = goal.target_amount
                messages.success(request, f"🎉 Congratulations! You've reached your goal '{goal.title}'!")
            else:
                messages.success(request, f"Added ${amount:.2f} to '{goal.title}'. Progress: {goal.progress_percent}%")

            goal.save()

        except (ValueError, TypeError):
            messages.error(request, "Invalid amount entered.")

        return HttpResponseRedirect(reverse('goals'))

    # Если не POST - перенаправляем на список целей
    return redirect('goals')


# НОВАЯ ФУНКЦИЯ: Удаление цели
def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)

    if request.method == "POST":
        goal_title = goal.title
        goal.delete()
        messages.success(request, f"Goal '{goal_title}' has been deleted.")
        return HttpResponseRedirect(reverse('goals'))

    # Если не POST - перенаправляем на список целей
    return redirect('goals')