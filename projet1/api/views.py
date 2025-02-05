from projet1.models import TodoEntry, Token
from .serializers import EntrySerializer
from .authentication import CustomTokenAuthentication
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated



@api_view(['GET'])
def testGet(request):
    test = {"test_key":1, "test_key_2":2}
    return Response(test)

@api_view(['GET'])
def getAllEntries(request):
    allEntries = TodoEntry.objects.all()
    serializer = EntrySerializer(allEntries, many=True)
    return JsonResponse({"entries" : serializer.data})

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def manage_token(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid credentials'}, status=400)

    if request.method == 'POST':
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=201 if created else 200)

    elif request.method == 'PUT':
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response({'token': token.key})

    elif request.method == 'DELETE':
        deleted, _ = Token.objects.filter(user=user).delete()
        if deleted:
            return Response({'message': 'Token deleted'})
        return Response({'error': 'No token found'}, status=404)

@api_view(['GET'])
@authentication_classes([CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def test_auth(request):
    return Response({'username': request.user.username})