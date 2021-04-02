from django.contrib import admin
from .models import Programme, Category


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'fixture',
        'date',
        'condition',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Category, CategoryAdmin)
