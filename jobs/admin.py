from django.contrib import admin
from .models import Jobs, Referencias


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", )

@admin.register(Referencias)
class ReferenciasAdmin(admin.ModelAdmin):
    pass