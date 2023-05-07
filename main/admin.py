from django.contrib import admin
from .models import Massage

@admin.register(Massage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'fifteen_minutes', 'thirty_minutes', 'forty_five_minutes', 'sixty_minutes',)
    search_fields = ('name', 'description',)
    list_filter = ('name',)
