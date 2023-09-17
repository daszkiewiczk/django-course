from django.contrib import admin

from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    list_filter = ('title', 'rating',)
    list_display = ('title', 'rating',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BookAdmin)


admin.site.register(Author)

admin.site.register(Address)

admin.site.register(Country)