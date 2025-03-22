from .models import BookReview
from django import forms


class BookReviewForm(forms.ModelForm):
    stars = forms.IntegerField(min_value=1,max_value=5)

    class Meta:
        model = BookReview
        fields = ('stars','comment')
