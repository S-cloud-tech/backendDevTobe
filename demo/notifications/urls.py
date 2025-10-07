from django.urls import path
from . import views

urlpatterns = [
    path('dropdown/', views.notification_dropdown, name='notification_dropdown'),
    path('mark-all-read/', views.mark_all_read, name='mark_all_read'),
    path('', views.notifications_list, name='notifications_list'),
]
