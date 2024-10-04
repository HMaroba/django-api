from django.contrib import admin
from .models import AuthorModel, NoteModel

# Register your models here.

admin.site.register(AuthorModel)
admin.site.register(NoteModel)

