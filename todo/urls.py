from django.urls import path

from .views import AboutUsView, tasksview, task_delete, cross_off, uncross, task_edit

urlpatterns = [
    path('', tasksview, name='home'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('delete/<int:pk>', task_delete, name='delete'),
    path('cross_off/<int:pk>', cross_off, name='cross_off'),
    path('uncross/<int:pk>', uncross, name='uncross'),
    path('edit/<int:pk>', task_edit, name='edit'),
]
