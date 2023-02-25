from django.urls import path

from .views import AboutUsView, tasksview

urlpatterns = [
    path('', tasksview, name='home'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),

]
