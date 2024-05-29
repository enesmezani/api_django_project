from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = 'authors'
        managed = False

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'genres'
        managed = False

    def __str__(self):
        return self.name
    
class Borrower(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'borrowers'
        managed = False

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrower = models.ForeignKey('Borrower', on_delete=models.CASCADE)
    check_out_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'transactions'
        managed = False

    def __str__(self):
        return self.book

class Language(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'languages'
        managed = False

    def __str__(self):
        return self.name
    

class BookCopy(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    status = models.ForeignKey('BookStatus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_copies'
        managed = False

    def __str__(self):
        return self.book


class BookStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'book_statuses'
        managed = False

    def __str__(self):
        return self.name
    
class BookReview(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = 'book_reviews'
        managed = False

    def __str__(self):
        return self.reviewer_name
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    genres = models.ManyToManyField('Genre')

    class Meta:
        db_table = 'books'
        managed = False

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'publishers'
        managed = False

    def __str__(self):
        return self.name
