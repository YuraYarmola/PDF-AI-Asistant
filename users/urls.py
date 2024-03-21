from django.urls import path

from .views import UserListView, UserCreateView, UserProfileView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
]