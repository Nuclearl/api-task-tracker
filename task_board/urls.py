from django.urls import path

from .views import BoardView, TaskView

urlpatterns = [
    path('boards/', BoardView.as_view()),
    path('boards/<int:pk>/', BoardView.as_view()),
    path('boards/<int:pk>/tasks/', TaskView.as_view())
]
