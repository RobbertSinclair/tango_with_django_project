from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'url']
    list_display = ('title', 'category', 'url')


admin.site.register(Page, PageAdmin)
