from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse('users:register'),
            data = {
                'username':'tester0',
                'first_name':"Azizbek",
                "last_name":"Ibrohimov",
                "email":"tester0@gmail.com",
                "password":'Azizbek1410'
            })
        user = User.objects.get(username="tester0")
        self.assertEqual(user.first_name,"Azizbek")
        self.assertEqual(user.last_name,"Ibrohimov")
        self.assertEqual(user.email,"tester0@gmail.com")
        self.assertNotEqual(user.password,'Azizbek1410')
        self.assertTrue(user.check_password('Azizbek1410'))


    def test_required_fields(self):
        """Agar username va password bo‘lmasa, forma xato bo‘lishi kerak"""
        response = self.client.post(
            reverse('users:register'),
            data={
                'first_name': 'Azizbek',
                'last_name': 'Ibrohimov',
                'email': 'tester0@gmail.com'
            }
        )

        # Agar sahifa redirect qilsa, qayta so‘rab olamiz
        if response.status_code == 302:
            response = self.client.get(reverse('users:register'))

        # Forma xatolarini tekshiramiz
        form = response.context.get('form')
        self.assertIsNotNone(form)  # Forma mavjudligini tekshiramiz
        self.assertFalse(form.is_valid())  # Forma noto‘g‘ri bo‘lishi kerak

        # Forma xatolarini tekshiramiz
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)
        self.assertEqual(form.errors['username'][0], 'This field is required.')
        self.assertEqual(form.errors['password'][0], 'This field is required.')

        # Baza tekshiruvi (foydalanuvchi yaratilmagan bo‘lishi kerak)
        self.assertEqual(User.objects.count(), 0)

    def test_invalid_email(self):
        """Noto‘g‘ri email yuborilganda forma xato bo‘lishi kerak"""
        response = self.client.post(
            reverse('users:register'),
            data={
                'first_name': 'Azizbek',
                'last_name': 'Inrohimov',
                'username': 'tester0',
                'email': 'invalid-email',  # Noto‘g‘ri email format
                'password': 'Azizbek1410'
            }
        )

        # Agar sahifa redirect qilsa, qayta so‘rab olamiz
        if response.status_code == 302:
            response = self.client.get(reverse('users:register'))

        # Forma xatolarini tekshiramiz
        form = response.context.get('form')
        self.assertIsNotNone(form)
        self.assertFalse(form.is_valid())

        # Email uchun xato xabarini tekshiramiz
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'][0], 'Enter a valid email address.')

        # Baza tekshiruvi (foydalanuvchi yaratilmagan bo‘lishi kerak)
        self.assertEqual(User.objects.count(), 0)


    def test_unique_username(self):
        self.client.post(
            reverse('users:register'),
            data = {
                'username':'tester0',
                'first_name':"Azizbek",
                "last_name":"Ibrohimov",
                "email":"tester0@gmail.com",
                "password":'Azizbek1410'
            })
        response=self.client.post(
            reverse('users:register'),
            data = {
                'username':'tester0',
                'first_name':"Azizbek1",
                "last_name":"Ibrohimov1",
                "email":"tester01@gmail.com",
                "password":'Azizbek14101'
            })
        form = response.context.get('form')
        self.assertIsNotNone(form)
        self.assertFalse(form.is_valid())

        # Xatoni tekshiramiz
        self.assertIn('username', form.errors)
        self.assertEqual(form.errors['username'][0], 'A user with that username already exists.')

        # Foydalanuvchilar soni 1 bo‘lishi kerak, chunki ikkinchi urinish muvaffaqiyatsiz bo‘lishi kerak
        self.assertEqual(User.objects.filter(username='tester0').count(), 1)