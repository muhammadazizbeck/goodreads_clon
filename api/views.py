from django.shortcuts import render,get_object_or_404
from .serializers import BookReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status,permissions
from books.models import BookReview

#ddd
# Create your views here.

class BookReviewListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        reviews = BookReview.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(reviews,request)
        serializer = BookReviewSerializer(page_obj,many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self,request):
        serializer = BookReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class BookReviewDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,id):
        review = get_object_or_404(BookReview,id=id)
        serializer = BookReviewSerializer(review)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        review = get_object_or_404(BookReview,id=id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,id):
        review = get_object_or_404(BookReview,id=id)
        serializer = BookReviewSerializer(instance=review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        review = get_object_or_404(BookReview,id=id)
        serializer = BookReviewSerializer(instance=review,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)