from django.urls import path
from .views import todo_views

urlpatterns = [
    path('dummy/',todo_views.todo_manager)
]
