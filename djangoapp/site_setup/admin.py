from django.contrib import admin
from site_setup import models
from django.http import HttpRequest


class MenuLinkInline(admin.TabularInline):
    model = models.MenuLink
    extra = 1


@admin.register(models.SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInline,

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not models.SiteSetup.objects.exists()
