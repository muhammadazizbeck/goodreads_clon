from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser
# from django.utils import timezone

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    cover_image = models.ImageField(default='default_cover_picture.png')

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BookAuthor(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='authors')
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} written by {self.author.first_name} {self.author.last_name}"
    
    def full_name(self):
        return f'{self.author.first_name} {self.author.last_name}'
    

class BookReview(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
    comment = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.stars} was give by {self.user.username}"
    
    


