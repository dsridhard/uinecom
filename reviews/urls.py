from django.urls import path
from .views import RatingListAPIView,ReviewListAPIView

urlpatterns = [
    path('api/ratings/', RatingListAPIView.as_view(), name='ratings'),
    path('api/reviews/', ReviewListAPIView.as_view(), name='reviews'),
]