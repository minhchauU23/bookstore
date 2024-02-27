from django.urls import path, include
from .views import (ProductAPIView,)

urlpatterns = [
    path('api/', ProductAPIView.as_view()),
    # path('api/<slug:>/', CategoryAPIView.as_view()),
]
