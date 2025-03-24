from django.shortcuts import render,get_object_or_404
from .serializers import BookReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from books.models import BookReview


# Create your views here.

class BookReviewListAPIView(APIView):
    def get(self,request):
        reviews = BookReview.objects.all()
        serializer = BookReviewSerializer(reviews,many=True)
        context = {
            'data':serializer.data,
            'status':'success'
        }
        return Response(context,status=status.HTTP_200_OK)
    
class BookReviewDetailAPIView(APIView):
    def get(self,request,id):
        review = get_object_or_404(BookReview,id=id)
        serializer = BookReviewSerializer(review)
        context = {
            'data':serializer.data,
            'status':'success'
        }
        return Response(context,status=status.HTTP_200_OK)
    
