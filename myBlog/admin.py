from django.contrib import admin
from myBlog.models import Book, Author, Publisher
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('firstName', 'lastName',)

class BookAdmin(admin.ModelAdmin):
    list_filter = ('publicationDate',)
    date_hierarchy = 'publicationDate'
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
