from django.urls import path
from . import views

urlpatterns = [
    path('', views.testGet),
    path('token/', views.manage_token, name='manage-token'),
    path('testAuth/', views.test_auth, name='test-auth'),
    path('entries/', views.entries, name='entries'),
    path('entries/<int:userid>/', views.entries, name='entries-details'),
]