from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import (CategoryAPIView,)

urlpatterns = [
    path('api/', CategoryAPIView.as_view()),
    # path('api/<slug:>/', CategoryAPIView.as_view()),
]
