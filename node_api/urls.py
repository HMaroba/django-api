from django.urls import path
from node_api.views import Notes, Authors, NoteDetail, AuthorDetail, Users

urlpatterns = [
    path('notes/', Notes.as_view()),
    path('notes/<str:pk>/', NoteDetail.as_view(), name='note-detail'),
    path('authors/', Authors.as_view()),
    path('users/', Users.as_view()),
    path('authors/<str:pk>/', AuthorDetail.as_view(), name='author-detail')
]