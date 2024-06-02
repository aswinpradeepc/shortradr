from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'generated_at', 'click_count')
    search_fields = ('short_code', 'original_url')
    list_filter = ('generated_at',)
    ordering = ('-generated_at',)