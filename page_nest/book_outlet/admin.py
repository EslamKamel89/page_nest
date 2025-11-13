from django.contrib import admin

from .models import Address, Author, Book


class BookAdmin(admin.ModelAdmin): # type: ignore
    # readonly_fields = ('slug',)
    prepopulated_fields = {
        "slug" : ('title' ,)
    }
    list_filter = ( 'rating' ,'is_bestselling')
    list_display = ('title' , 'author' , 'rating' , 'is_bestselling')

admin.site.register(Book , BookAdmin)

class AuthorAdmin(admin.ModelAdmin) : # type: ignore
    list_display = ('first_name' , 'last_name' )

admin.site.register(Author , AuthorAdmin)


class AddressAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('street' , 'postal_code' , 'city')

admin.site.register(Address , AddressAdmin)
