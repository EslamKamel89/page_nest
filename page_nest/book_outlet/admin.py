from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {
        "slug" : ('title' ,)
    }
    list_filter = ( 'rating' ,'is_bestselling')
    list_display = ('title' , 'author' , 'rating' , 'is_bestselling')

admin.site.register(Book , BookAdmin)
