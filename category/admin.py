from django.contrib import admin
# Register your models here.

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}   #for automatic generating the slugs

admin.site.register(Category,CategoryAdmin)