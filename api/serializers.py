from books.models import CustomUser,Book,BookReview
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','first_name','last_name','email')

    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','description','isbn')


class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True,required=False)
    user_id = serializers.IntegerField(write_only=True,required=False)

    class Meta:
        model = BookReview
        fields = ('book','user','comment','stars','book_id','user_id')