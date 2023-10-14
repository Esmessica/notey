from django.urls import path
from . import views

app_name = 'notey_app'


urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('notes/', views.NotesView.as_view(), name="notes"),
    path('mood/', views.MoodView.as_view(), name="mood"),
]