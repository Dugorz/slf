from django.contrib import admin
from .models import *


class WorkerModelAdmin(admin.ModelAdmin):
    fields = ('worker_name', 'worker_photo', 'worker_portfolio')
    list_display = ('worker_name', 'created')
    ordering = ('worker_name', )


admin.site.register(WorkersModel, WorkerModelAdmin)
