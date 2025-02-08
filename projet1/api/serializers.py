from rest_framework import serializers
from projet1.models import TodoEntry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoEntry
        fields = ["id","user","entryid","name","dateCreated","completed"]
        extra_kwargs = {
            'user': {'required': False},
            'dateCreated': {'required': False},
            'completed': {'required': False},
        }