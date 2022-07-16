from django.contrib import admin
from .models import Imovel, Category, Photo

class CategoryAdmin(admin.ModelAdmin):
    ...

class PhotoAdmin(admin.ModelAdmin):
    model = Photo

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

admin.site.register(Category, CategoryAdmin)

