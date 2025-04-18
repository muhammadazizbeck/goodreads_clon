from django.shortcuts import render,redirect,get_object_or_404
from .models import Book,BookReview
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.views import View
from .forms import BookReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
        
    
class ReviewUpdateView(LoginRequiredMixin,View):
    def get(self,request,book_id,review_id):
        book = get_object_or_404(Book,id=book_id)
        review = get_object_or_404(BookReview,id=review_id,book=book)
        edit_form = BookReviewForm(instance=review)

        context = {
            'book':book,
            'review':review,
            'edit_form':edit_form
        }
        return render(request,'books/edit_review.html',context)
    
    def post(self,request,book_id,review_id):
        book = get_object_or_404(Book,id=book_id)
        review = get_object_or_404(BookReview,id=review_id,book=book)
        edit_form = BookReviewForm(instance=review,data=request.POST)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,'You have successfully updated your review')
            return redirect(reverse('books:detail',kwargs={'id':book.id}))
        else:
            context = {
                'edit_form':edit_form
            }
            return render(request,'books/detail.html',context)
        
class DeleteReview(LoginRequiredMixin,View):
    def get(self,request,book_id,review_id):
        book = get_object_or_404(Book,id=book_id)
        review = get_object_or_404(BookReview,id=review_id,book=book)
        review.delete()
        messages.success(request,'You have successfully deleted your review')
        return redirect(reverse('books:detail',kwargs={'id':book.id}))
        
            

    

