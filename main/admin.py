from django.contrib import admin
from .models import *


class WorkerModelAdmin(admin.ModelAdmin):
    fields = ('worker_name', 'worker_photo', 'worker_portfolio', 'slug', 'genre', 'description')
    list_display = ('worker_name', 'created')
    ordering = ('worker_name', )
    prepopulated_fields = {'slug': ('worker_name', )}


class GenreModelAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'cover', 'photo_examples')
    list_display = ('name', )
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name', )}


class ImageModelAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'slug')
    list_display = ('name', )
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(WorkersModel, WorkerModelAdmin)
admin.site.register(Genre, GenreModelAdmin)
admin.site.register(Image, ImageModelAdmin)
