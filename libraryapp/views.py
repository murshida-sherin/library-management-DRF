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
    
    
class BorrowedBooks(APIView):
    def get(self,request,*args,**kwargs):
        Borrowed=BorrowRecord.objects.filter(is_returned="False")
        
        serializer=BorrowSerializer(Borrowed,many=True)
        return Response({'borrowed_books':serializer.data})      