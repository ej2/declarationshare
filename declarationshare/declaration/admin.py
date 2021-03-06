from django.contrib import admin

from declarationshare.declaration.models import Declaration


class DeclarationModelAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "text", "ip_address", "author", "anonymous")
    search_fields = ("id", "text",)
    list_per_page = 50

admin.site.register(Declaration, DeclarationModelAdmin)
