from django.urls import path

from . import views

app_name = 'messageBox'
urlpatterns = [
    path('user/register/', views.register, name='register'),
]
