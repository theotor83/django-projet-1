from django.http import JsonResponse
from projet1.models import TodoEntry
from .serializers import EntrySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def testGet(request):
    test = {"test_key":1, "test_key_2":2}
    return Response(test)

@api_view(['GET'])
def getAllEntries(request):
    allEntries = TodoEntry.objects.all()
    serializer = EntrySerializer(allEntries, many=True)
    return JsonResponse({"entries" : serializer.data})