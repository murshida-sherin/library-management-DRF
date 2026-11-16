from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    category=models.CharField(max_length=20)
    isbn=models.CharField(max_length=20)
    available_copies=models.IntegerField()
    
    def __str__(self):
        return f"{self.title}"
    
class BorrowRecord(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    borrower_name=models.CharField(max_length=20)
    borrower_email=models.EmailField()
    borrow_date=models.DateField()
    is_returned=models.BooleanField()