from django.test import TestCase
from books.models import Book
from django.urls import reverse
# Create your tests here.

class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response,'No books found.')

    def test_books_list(self):
        Book.objects.create(title='Book1',description='Description1',isbn='12345')
        Book.objects.create(title='Book2',description='Description2',isbn='12346')
        Book.objects.create(title='Book3',description='Description3',isbn='12347')

        response = self.client.get(reverse('books:list'))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response,book.title)

    def test_book_detail(self):
        book = Book.objects.create(title='Book1',description='Description1',isbn='98475')
        response = self.client.get(reverse('books:detail',kwargs={'id':book.id}))

        self.assertContains(response,book.title)
        self.assertContains(response,book.description)

    def test_search_books(self):
        book1 = Book.objects.create(title='noname',description='Description1',isbn='12345')
        book2 = Book.objects.create(title='somename',description='Description2',isbn='12346')

        response1 = self.client.get(reverse('books:list')+"?q=noname")
        
        self.assertContains(response1,book1.title)
        self.assertNotContains(response1,book2.title)


        response2 = self.client.get(reverse('books:list')+"?q=somename")

        self.assertContains(response2,book2.title)
        self.assertNotContains(response2,book1.title)


