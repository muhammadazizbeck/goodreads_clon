
from django.urls import path
from .views import BookListView,BookDetailView,AddReviewView


app_name='books'
urlpatterns = [
    path('',BookListView.as_view(),name='list'),
    path('<int:id>/',BookDetailView.as_view(),name='detail'),
    path('<int:id>/reviews/',AddReviewView.as_view(),name='reviews')
]