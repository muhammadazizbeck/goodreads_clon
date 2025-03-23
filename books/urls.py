
from django.urls import path
from .views import BookListView,BookDetailView,AddReviewView,ReviewUpdateView,DeleteReview


app_name='books'
urlpatterns = [
    path('',BookListView.as_view(),name='list'),
    path('<int:id>/',BookDetailView.as_view(),name='detail'),
    path('<int:id>/reviews/',AddReviewView.as_view(),name='reviews'),
    path('<int:book_id>/reviews/<int:review_id>/edit/',ReviewUpdateView.as_view(),name='update-review'),
    path('<int:book_id>/reviews/<int:review_id>/delete/',DeleteReview.as_view(),name='delete-review')
]