from rest_framework import serializers
from libraryapp.models import Book,BorrowRecord

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
        
class BorrowSerializer(serializers.ModelSerializer):
    book=serializers.SerializerMethodField
    
    class Meta:
        model=BorrowRecord
        fields="__all__"
        read_only_fields=['id','owner']
        
    def get_book(self,obj):
        book=obj.book
        queryset=Book.objects.all()
        return {'book':book}