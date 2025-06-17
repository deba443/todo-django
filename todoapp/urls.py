from django.urls import path
from .views import todo_views

urlpatterns = [
    # path('crud/',todo_views.todo_manager)
    path('crud/',todo_views.MyModelApiView.as_view()),
    path('crud/<int:pk>/',todo_views.MyModelApiView.as_view())
]
