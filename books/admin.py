from django.contrib import admin

from books.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender')
    list_filter = ('gender', )


admin.site.register(Author, AuthorAdmin)





