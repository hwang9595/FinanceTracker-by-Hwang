# FinanceTracker/urls.py
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language  # ← импортируем

from home import views as home_views
from transactions import views as transactions_views
from categories import views as categories_views
from goals import views as goals_views
from users import views as users_views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('set_language/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('transactions/', transactions_views.transaction_list, name='transactions'),
    path('transactions/delete/<int:transaction_id>/', transactions_views.delete_transaction, name='delete_transaction'),
    path('categories/', categories_views.category_list, name='categories'),
    path('categories/delete/<int:category_id>/', categories_views.delete_category, name='delete_category'),
    path('goals/', goals_views.goal_list, name='goals'),
    path('goals/add-savings/<int:goal_id>/', goals_views.add_savings, name='add_savings'),
    path('goals/delete/<int:goal_id>/', goals_views.delete_goal, name='delete_goal'),
    path('users/', users_views.users, name='users'),

)