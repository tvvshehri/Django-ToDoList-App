from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Delete/<str:pk>', views.Delete, name='Delete'),
    path('Done/<str:pk>', views.Done, name='Done'),
    path('Active/<str:pk>', views.Active, name='Active')
]
