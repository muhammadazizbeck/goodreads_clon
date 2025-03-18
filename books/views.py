from django.shortcuts import render
from .models import Book
from django.views import View

# Create your views here.

class BookListView(View):
    def get(self,request):
        books = Book.objects.all()
        context = {
            'books':books
        }
        return render(request,'books/list.html',context)
    

class BookDetailView(View):
    def get(self,request,id):
        book = Book.objects.get(id=id)
        context = {
            'book':book
        }
        return render(request,'books/detail.html',context)
    

