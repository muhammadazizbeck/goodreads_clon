from . import views
from django.urls import path

urlpatterns = [
    path('reviews/',views.BookReviewListAPIView.as_view(),name='review-list'),
    path('reviews/<int:id>/',views.BookReviewDetailAPIView.as_view(),name='review-detail')
]