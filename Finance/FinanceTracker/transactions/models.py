from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

from categories.models import Category

class Transaction(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'

    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    title = models.CharField(max_length=100)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=EXPENSE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='transactions',
        null=True,
        blank=True
    )
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date', '-created_at',)

    def __str__(self):
        return f'{self.title} {self.amount}'