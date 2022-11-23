from django.db import models

class Author(models.Model):
    author_code = models.AutoField(db_column='Author_code', primary_key=True)  # Field name made lowercase.
    author_name = models.CharField(db_column='Author_name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    book_code = models.AutoField(db_column='Book_code', primary_key=True)  # Field name made lowercase.
    isbn = models.ForeignKey('BookInfo', models.DO_NOTHING, db_column='ISBN')  # Field name made lowercase.
    location_code = models.ForeignKey('BookLocation', models.DO_NOTHING, db_column='Location_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class BookAuthor(models.Model):
    isbn = models.OneToOneField('BookInfo', models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase.
    author_code = models.ForeignKey(Author, models.DO_NOTHING, db_column='Author_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_author'
        unique_together = (('isbn', 'author_code'),)


class BookCategory(models.Model):
    isbn = models.OneToOneField('BookInfo', models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase.
    category_code = models.ForeignKey('Category', models.DO_NOTHING, db_column='Category_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_category'
        unique_together = (('isbn', 'category_code'),)


class BookInfo(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=45)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=45)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=45, blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=45)  # Field name made lowercase.
    public_year = models.CharField(db_column='Public_year', max_length=45)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    publisher_code = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='Publisher_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_info'


class BookLocation(models.Model):
    location_code = models.AutoField(db_column='Location_code', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_location'


class BookManage(models.Model):
    book_code = models.IntegerField(db_column='Book_code', primary_key=True)  # Field name made lowercase.
    man_code = models.ForeignKey('Manager', models.DO_NOTHING, db_column='Man_code')  # Field name made lowercase.
    isrental = models.CharField(db_column='IsRental', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_manage'


class Category(models.Model):
    category_code = models.AutoField(db_column='Category_code', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='Category_name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Manager(models.Model):
    man_code = models.AutoField(db_column='Man_code', primary_key=True)  # Field name made lowercase.
    man_name = models.CharField(db_column='Man_name', max_length=45)  # Field name made lowercase.
    man_phone = models.CharField(db_column='Man_phone', max_length=45)  # Field name made lowercase.
    man_email = models.CharField(db_column='Man_email', max_length=45)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=45)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manager'


class Member(models.Model):
    mem_code = models.AutoField(db_column='Mem_code', primary_key=True)  # Field name made lowercase.
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
    publisher_code = models.AutoField(db_column='Publisher_code', primary_key=True)  # Field name made lowercase.
    publisher_name = models.CharField(db_column='Publisher_name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publisher'


class Rental(models.Model):
    rental_code = models.AutoField(db_column='Rental_code', primary_key=True)  # Field name made lowercase.
    mem_code = models.ForeignKey(Member, models.DO_NOTHING, db_column='Mem_code')  # Field name made lowercase.
    book_code = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_code')  # Field name made lowercase.
    rental_date = models.DateTimeField(db_column='Rental_date')  # Field name made lowercase.
    due_date = models.CharField(db_column='Due_date', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rental'


class Request(models.Model):
    request_code = models.AutoField(db_column='Request_code', primary_key=True)  # Field name made lowercase.
    mem_code = models.ForeignKey(Member, models.DO_NOTHING, db_column='Mem_code')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=45)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request'


class Return(models.Model):
    return_code = models.AutoField(db_column='Return_code', primary_key=True)  # Field name made lowercase.
    mem_code = models.ForeignKey(Member, models.DO_NOTHING, db_column='Mem_code')  # Field name made lowercase.
    book_code = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_code')  # Field name made lowercase.
    return_date = models.CharField(db_column='Return_date', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'return'
