from django.contrib import admin
from .models import Scholarship


class ScholarshipAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Scholarship, ScholarshipAdmin)
