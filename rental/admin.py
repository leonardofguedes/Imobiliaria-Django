from django.contrib import admin
from .models import Imovel, Category, Photo

class CategoryAdmin(admin.ModelAdmin):
    ...

class PhotoAdmin(admin.ModelAdmin):
    model = Photo

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    ...

admin.site.register(Photo)
admin.site.register(Category, CategoryAdmin)

