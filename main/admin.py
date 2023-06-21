from django.contrib import admin
from .models import *

@admin.register(Massage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'fifteen_minutes', 'thirty_minutes', 'forty_five_minutes', 'sixty_minutes',)
    search_fields = ('name', 'description',)
    list_filter = ('name',)

@admin.register(Service)
class ServiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)
    search_fields = ('name', 'description',)
    list_filter = ('name',)

@admin.register(Sertificats)
class  SertAdmin(admin.ModelAdmin):
    list_display = ('view', 'description', 'price',)
    search_fields = ('view', 'description',)

@admin.register(Banks)
class BanksAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','create_date',)
    readonly_fields = ('create_date',)
    search_fields = ('name','text',)
    list_filter= ('create_date',)


@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('name_massage','text',)
    