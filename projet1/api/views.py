from rest_framework.response import Response
from rest_framework.decorator import api_view

@api_view(['GET'])
def testGet(request):
    test = {"test_key":1, "test_key_2":2}
    return Response(test)