from django.contrib import admin

from .models import Address, Author, Book, Country


@admin.register(Book)
class BookAdmin(admin.ModelAdmin): # type: ignore
    # readonly_fields = ('slug',)
    prepopulated_fields = {
        "slug" : ('title' ,)
    }
    list_filter = ( 'rating' ,'is_bestselling')
    list_display = ('title' , 'author' , 'rating' , 'is_bestselling')
    filter_horizontal = ('published_countries' ,)

# admin.site.register(Book , BookAdmin)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin) : # type: ignore
    list_display = ('first_name' , 'last_name' )

# admin.site.register(Author , AuthorAdmin)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('street' , 'postal_code' , 'city')
    list_filter = ('city',)

# admin.site.register(Address , AddressAdmin)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('name' , 'code')
# admin.site.register(Country  , CountryAdmin)
