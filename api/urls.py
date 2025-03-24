from . import views
from django.urls import path


app_name='api'
urlpatterns = [
    path('reviews/',views.BookReviewListAPIView.as_view(),name='review-list'),
    path('reviews/<int:id>/',views.BookReviewDetailAPIView.as_view(),name='review-detail')
]