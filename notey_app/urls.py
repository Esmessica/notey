from django.urls import path
from . import views

app_name = 'notey_app'


urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('notes/', views.NotesView.as_view(), name="notes"),
    path('mood/', views.MoodView.as_view(), name="mood"),
    path('mood_advice/', views.SaveMoodView.as_view(), name='mood_advice'),
    path('note/', views.NoteListView.as_view(), name='all_notes'),
    path('note/add', views.CreateNoteView.as_view(), name='create_note'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('note/<int:pk>/edit', views.NoteUpdateView.as_view(), name='note_edit'),
    path('note/<int:pk>/delete', views.NoteDeleteView.as_view(), name='note_delete'),
    path('draw/', views.DrawView.as_view(), name='draw')
]