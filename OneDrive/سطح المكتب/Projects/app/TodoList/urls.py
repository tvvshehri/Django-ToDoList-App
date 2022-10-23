from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('done/<str:pk>', views.done, name='done')
]
