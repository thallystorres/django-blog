from django.contrib import admin
from site_setup import models
from django.http import HttpRequest

@admin.register(models.MenuLink)
class MenuLink(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path',
    list_display_links = 'id', 'text', 'url_or_path',
    search_fields = 'id', 'text', 'url_or_path',
    ordering = '-id',


@admin.register(models.SiteSetup)
class SiteSetup(admin.ModelAdmin):
    list_display = 'title', 'description',

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not models.SiteSetup.objects.exists()
