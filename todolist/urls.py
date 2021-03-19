from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'),
]