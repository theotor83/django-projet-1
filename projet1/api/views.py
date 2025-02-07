from projet1.models import TodoEntry, Token
from .serializers import EntrySerializer
from .authentication import CustomTokenAuthentication
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated




@api_view(['GET'])
def testGet(request):
    test = {"test_key":1, "test_key_2":2}
    return Response(test)


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
    return Response({'userid': request.user.id})

@api_view(['GET', 'POST'])
@authentication_classes([CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def entries(request, requestedUserId = None):

    if requestedUserId == None: #if /api/entries/ instead of /api/entries/<id>
        if request.method == 'GET':
            if request.user.id == 1: #admin
                allEntries = TodoEntry.objects.all()
                serializer = EntrySerializer(allEntries, many=True)
                return JsonResponse({"entries" : serializer.data}, status=200)
            else:
                return Response({'error': '403 Unauthorized'}, status=403)
            
    else:
        if request.method == 'GET':
            if request.user.id == requestedUserId or request.user.id == 1 : #1 = admin
                requestedUserId = get_object_or_404(User, pk=requestedUserId)
                entries = TodoEntry.objects.filter(user=requestedUserId)
                serializer = EntrySerializer(entries, many=True)
                return JsonResponse({"entries" : serializer.data}, status=200)
            else:
                return JsonResponse({'error': '403 Unauthorized'}, status=403)
        if request.method == 'POST':
            if request.user.id == requestedUserId or request.user.id == 1 : #1 = admin
                requestedUserId = get_object_or_404(User, pk=requestedUserId)
                serializer = EntrySerializer(data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save(user=requestedUserId)
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
            else:
                return JsonResponse({'error': '403 Unauthorized'}, status=403)