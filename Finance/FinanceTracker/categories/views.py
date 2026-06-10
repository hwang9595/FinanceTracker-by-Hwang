from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CategoryForm
from .models import Category


def category_list(request):
    form = CategoryForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Category added successfully!")
        return redirect('categories')

    categories = Category.objects.all()

    return render(
        request,
        'category_list.html',
        {'categories': categories,
         'form': form,
         }
    )


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        category_name = category.name
        category.delete()
        messages.success(request, f"Category '{category_name}' has been deleted.")
        return redirect('categories')

    return redirect('categories')