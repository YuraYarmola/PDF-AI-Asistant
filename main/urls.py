from django.urls import path
from .views import *

urlpatterns = [
    path('user/<int:pk>/upload/', FileUploadView.as_view(), name='file_upload'),
    path("user/<int:pk>/prompt/", PromptView.as_view(), name='prompt')
]