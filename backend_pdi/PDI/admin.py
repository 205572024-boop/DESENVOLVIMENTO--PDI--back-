from django.contrib import admin
from.models import PDI
@admin.register(PDI)
class PDIAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at", "updated_at")
    search_fields = ("name", "description")
    list_filter = ("created_at", "updated_at")