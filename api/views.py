from django.shortcuts import render,get_object_or_404
from .serializers import BookReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status,permissions
from books.models import BookReview


# Create your views here.

class BookReviewListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        reviews = BookReview.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(reviews,request)
        serializer = BookReviewSerializer(page_obj,many=True)
        return paginator.get_paginated_response(serializer.data)


    
class BookReviewDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,id):
        review = get_object_or_404(BookReview,id=id)
        serializer = BookReviewSerializer(review)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
