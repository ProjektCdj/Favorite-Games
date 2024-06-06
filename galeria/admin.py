from django.contrib import admin
from galeria.models import Thumb


class ListandoThumbs(admin.ModelAdmin):
    list_display = ("id", "nome", "plataforma", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria", "usuario",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Thumb, ListandoThumbs)
