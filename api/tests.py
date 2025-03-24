from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from users.models import CustomUser
from books.models import Book,BookReview

# Create your tests here.

class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='tester0',email='tester0@gmail.com')
        self.user.set_password('Azizbek1410')
        self.user.save()
        self.client.login(username='tester0',password='Azizbek1410')

    def test_book_review_detail(self):
        book = Book.objects.create(title='Book1',description='Description1',isbn='123456')
        review = BookReview.objects.create(book=book,user=self.user,stars=4,comment='Very good book')

        response = self.client.get(reverse('api:review-detail',kwargs={'id':review.id}))

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['comment'],'Very good book')
        self.assertEqual(response.data['stars'],4)
        self.assertEqual(response.data['book']['title'],'Book1')
        self.assertEqual(response.data['book']['description'],'Description1')
        self.assertEqual(response.data['user']['username'],'tester0')
        self.assertEqual(response.data['user']['email'],'tester0@gmail.com')

    def test_book_review_list(self):
        book = Book.objects.create(title='Book1',description='Description1',isbn='123456')
        review1 = BookReview.objects.create(book=book,user=self.user,stars=5,comment='good')
        review2 = BookReview.objects.create(book=book,user=self.user,stars=4,comment='nice')

        response = self.client.get(reverse('api:review-list'))

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['count'],2)
        self.assertIn('next',response.data)
        self.assertIn('previous',response.data)
        self.assertEqual(response.data['results'][0]['comment'],review2.comment)
        self.assertEqual(response.data['results'][1]['comment'],review1.comment)



