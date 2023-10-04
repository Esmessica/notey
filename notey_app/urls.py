from django.urls import path
from . import views

app_name = 'notey_app'


urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
]