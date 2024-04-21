from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_view, name='todo'),
    path('delete/<int:pk>', views.delete_view, name='delete'),
    path('finished/<int:pk>', views.finished_view, name='finished'),
]