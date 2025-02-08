from rest_framework import serializers
from projet1.models import TodoEntry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoEntry
        fields = ["id","user","entryid","name","dateCreated","completed"]
        extra_kwargs = {
            'id': {'required': False},
            'user': {'required': False},
            'entryid': {'required': False},
            'name': {'required': False},
            'dateCreated': {'required': False},
            'completed': {'required': False},
        }
        read_only_fields = ['user', 'entryid', 'id', 'dateCreated']