from django.db import models

class Author(models.Model):
    author_code = models.IntegerField(db_column='Author_code', primary_key=True)  # Field name made lowercase.
    author_name = models.CharField(db_column='Author_name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    book_code = models.AutoField(db_column='Book_code', primary_key=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=45)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=45)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=45)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=45)  # Field name made lowercase.
    public_year = models.CharField(db_column='Public_year', max_length=45)  # Field name made lowercase.
    location_code = models.ForeignKey('BookLocation', models.DO_NOTHING, db_column='Location_code')  # Field name made lowercase.
    publisher_code = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='Publisher_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'
        unique_together = (('book_code', 'isbn'),)


class BookAuthor(models.Model):
    book_code = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_code', primary_key=True)  # Field name made lowercase.
    author_code = models.ForeignKey(Author, models.DO_NOTHING, db_column='Author_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_author'
        unique_together = (('book_code', 'author_code'),)


class BookCategory(models.Model):
    book_code = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_code', primary_key=True)  # Field name made lowercase.
    category_code = models.ForeignKey('Category', models.DO_NOTHING, db_column='Category_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_category'
        unique_together = (('book_code', 'category_code'),)


class BookLocation(models.Model):
    location_code = models.IntegerField(db_column='Location_code', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_location'


class BookManage(models.Model):
    book_code = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_code', primary_key=True)  # Field name made lowercase.
    man_code = models.ForeignKey('Manager', models.DO_NOTHING, db_column='Man_code')  # Field name made lowercase.
    isrental = models.CharField(db_column='IsRental', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_manage'
        unique_together = (('book_code', 'man_code'),)


class Category(models.Model):
    category_code = models.IntegerField(db_column='Category_code', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='Category_name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Manager(models.Model):
    man_code = models.IntegerField(db_column='Man_code', primary_key=True)  # Field name made lowercase.
    man_name = models.CharField(db_column='Man_name', max_length=45)  # Field name made lowercase.
    man_phone = models.CharField(db_column='Man_phone', max_length=45)  # Field name made lowercase.
    man_email = models.CharField(db_column='Man_email', max_length=45)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=45)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manager'


class Member(models.Model):
    mem_code = models.IntegerField(db_column='Mem_code', primary_key=True)  # Field name made lowercase.
    mem_name = models.CharField(db_column='Mem_name', max_length=45)  # Field name made lowercase.
    mem_gender = models.CharField(db_column='Mem_gender', max_length=45)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=45)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=45)  # Field name made lowercase.
    mem_email = models.CharField(db_column='Mem_email', max_length=45)  # Field name made lowercase.
    mem_phone = models.CharField(db_column='Mem_phone', max_length=45)  # Field name made lowercase.
    mem_address = models.CharField(db_column='Mem_address', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class Publisher(models.Model):
    publisher_code = models.IntegerField(db_column='Publisher_code', primary_key=True)  # Field name made lowercase.
    publisher_name = models.CharField(db_column='Publisher_name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publisher'


class Rental(models.Model):
    mem_code = models.OneToOneField(Member, models.DO_NOTHING, db_column='Mem_code', primary_key=True)  # Field name made lowercase.
    mem_code = models.OneToOneField(Member, models.DO_NOTHING, db_column='Mem_code', primary_key=True)  # Field name made lowercase.
    book_code = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_code')  # Field name made lowercase.
    return_date = models.CharField(db_column='Return_date', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'return'
        unique_together = (('mem_code', 'book_code'),)
