from django.urls import path
from . import views

urlpatterns = [
    path('', views.testGet),
    path('token/', views.manage_token, name='manage-token'),
    path('testAuth/', views.test_auth, name='test-auth'),
    path('entries/', views.entries, name='entries'),
    path('entries/<int:requestedUserId>/', views.entries, name='entries-user'),
    path('entries/<int:requestedUserId>/<int:requestedEntryId>', views.entries, name='entries-user-details'),
]