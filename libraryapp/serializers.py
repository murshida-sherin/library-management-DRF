from rest_framework import serializers
from libraryapp.models import Book,BorrowRecord


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
        
class BorrowSerializer(serializers.ModelSerializer):
    book=serializers.SerializerMethodField()
    
    class Meta:
        model=BorrowRecord
        fields="__all__"
        
    def get_book(self,obj):
        return obj.book.title