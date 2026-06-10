from django.contrib import admin
from categories.models import Category
from .models import Transaction
from goals.models import Goal


admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Goal)



# Register your models here.
