from django.contrib import admin

from blog import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name',
    search = 'id', 'name', 'slug'
    ordering = '-id',
    list_per_page = 10
    prepopulated_fields = {
        "slug": ('name',),
    }
