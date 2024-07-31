from rest_framework import serializers
from node_api.models import NoteModel, AuthorModel


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'
