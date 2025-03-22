from django.shortcuts import render,redirect
from .models import Book,BookReview
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views import View
from .forms import BookReviewForm

# Create your views here.

class BookListView(View):
    def get(self,request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q','')
        if search_query:
            books = books.filter( Q(title__icontains=search_query) | Q(isbn__icontains=search_query))
        paginator = Paginator(books,6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj':page_obj,
            'search_query':search_query
        }
        return render(request,'books/list.html',context)
    

class BookDetailView(View):
    def get(self,request,id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()
        context = {
            'book':book,
            'review_form':review_form
        }
        return render(request,'books/detail.html',context)
    
class AddReviewView(View):
    def post(self,request,id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)
        if review_form.is_valid():
            BookReview.objects.create(
                book = book,
                user = request.user,
                stars = review_form.cleaned_data['stars'],
                comment = review_form.cleaned_data['comment']
            )
            return redirect(reverse('books:detail',kwargs={'id':book.id}))
        else:
            context = {
                'review_form':review_form
            }
            return render(request,'books/detail.html',context)
    

