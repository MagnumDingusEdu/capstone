from django.contrib import admin
from .models import Scholarship


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name",
        # "active",
        "scholarship_type",
    ]

    readonly_fields = ("created_at", "updated_at")

