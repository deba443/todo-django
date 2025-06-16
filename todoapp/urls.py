from django.urls import path
from .views import todo_views

urlpatterns = [
    path('crud/',todo_views.todo_manager)
]
