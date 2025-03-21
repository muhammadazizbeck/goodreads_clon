from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.core.paginator import Paginator
from django.views import View

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
        context = {
            'book':book
        }
        return render(request,'books/detail.html',context)
    

