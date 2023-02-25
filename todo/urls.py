from django.urls import path

from .views import AboutUsView, tasksview, task_delete

urlpatterns = [
    path('', tasksview, name='home'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('delete/<int:pk>', task_delete, name='delete'),

]
