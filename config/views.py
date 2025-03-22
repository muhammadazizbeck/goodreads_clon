from django.shortcuts import render
from books.models import BookReview
from django.core.paginator import Paginator


def landing_page(request):
    return render(request,'landing.html')

def allreview_page(request):
    reviews = BookReview.objects.all().order_by('-created_at')
    paginator = Paginator(reviews,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return render(request,'allreview.html',context)