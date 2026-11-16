from django.shortcuts import render
from libraryapp.models import Book,BorrowRecord
from libraryapp.serializers import BookSerializer,BorrowSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CreateListBookView(CreateAPIView,ListAPIView):
    serializer_class=BookSerializer
    queryset=Book.objects.all()
    
    
class RetrieveUpdateDeleteBookView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=BookSerializer
    queryset=Book.objects.all()
    
    
class CreateListBorrow(CreateAPIView,ListAPIView):
    serializer_class=BorrowSerializer
    queryset=BorrowRecord.objects.all()
    
class RetrieveUpdateDestroyBorrow(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=BorrowSerializer
    queryset=BorrowRecord.objects.all() 
    
    
class BorrowedBooksView(APIView):
    def get(self,request,*args,**kwargs):
        borrowed=BorrowRecord.objects.filter(is_returned="False")
        
        return Response({'borrowed books':borrowed})      