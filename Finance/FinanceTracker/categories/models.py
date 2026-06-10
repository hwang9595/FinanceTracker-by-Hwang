from django.db import models

from django.db import models
from django.conf import settings


class Category(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'

    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    name = models.CharField(max_length=80)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=EXPENSE)
    color = models.CharField(max_length=7, default='#2563eb')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='category',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['type', 'name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.type} {self.name}'

# Create your models here.
