from rest_framework import serializers
from projet1.models import TodoEntry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoEntry
        fields = ["id","user","name","dateCreated","completed"]