# from django.urls import path
# from node_api.views import Notes, NoteDetail

# urlpatterns = [
#     path('', Notes.as_view()),
#     path('<str:pk>', NoteDetail.as_view())
# ]

from django.urls import path
from node_api.views import Notes, NoteDetail, AuthorDetail

urlpatterns = [
    path('', Notes.as_view(), name='notes'),
    path('notes/<str:pk>/', NoteDetail.as_view(), name='note-detail'),
    # path('authors/', Authors.as_view(), name='authors'),
    path('authors/<str:pk>/', AuthorDetail.as_view(), name='author-detail')
]