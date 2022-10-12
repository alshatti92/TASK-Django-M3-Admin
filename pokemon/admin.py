from django.contrib import admin
from .models import Pokemon

# Register your models here.


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hp", "active",)
    list_display_links = ("id", "name",)
    list_filter = ("active",)

    fieldsets = (
        (
            "localisation", {
                "field": ("name_ar", "name_fr", "name_jp", ),
                "classes": ("collapse",)})
    )
