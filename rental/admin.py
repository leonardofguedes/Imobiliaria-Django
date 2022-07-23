from django.contrib import admin
from .models import ModelImage, Imovel


class ModelImageAdmin(admin.StackedInline):
    model = ModelImage


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'created_at']
    list_display_links = ('title',)
    search_fields = 'category', 'id', 'title', 'description', 'city'
    list_filter = 'category', 'author', 'is_published', 'city'
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title','city',)
    }
    inlines = [ModelImageAdmin]

@admin.register(ModelImage)
class ModelImageAdmin(admin.ModelAdmin):
    pass
