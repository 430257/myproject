from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Database


@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "created_at", "updated_at"]

