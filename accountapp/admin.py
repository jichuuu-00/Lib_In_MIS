from django.contrib import admin

# Register your models here.
from accountapp.models import Member, Manager, Rental, Return, BookLocation, Author, Book, BookAuthor, BookCategory, \
    BookInfo, BookManage, Category, Publisher

admin.site.register(Member)
admin.site.register(Manager)
admin.site.register(Rental)
admin.site.register(Return)
admin.site.register(BookLocation)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(BookCategory)
admin.site.register(BookInfo)
admin.site.register(BookManage)
admin.site.register(Category)
admin.site.register(Publisher)
