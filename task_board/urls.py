from django.urls import path

from .views import BoardView, TaskView

urlpatterns = [
    path('boards/', BoardView.as_view()),
    path('boards/<int:pk>/', BoardView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>', TaskView.as_view()),
    path('tasks/<int:pk>/<int:pk1>/', TaskView.as_view())
]
