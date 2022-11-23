from django.contrib import admin
from .models import Scholarship, ScholarshipConstraint, Constraint, Notice, NoticeCategory


class ScholarshipConstraintInlineAdmin(admin.StackedInline):
    model = ScholarshipConstraint
    extra = 1


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    inlines = [ScholarshipConstraintInlineAdmin]
    list_display = (
        'name',
        'scholarship_type',
        'enabled',
        'amount',
        'notes'
    )
    list_filter = ('enabled', 'created_at', 'updated_at', 'scholarship_type')
    raw_id_fields = ('constraints',)
    search_fields = ('name', 'notes')
    date_hierarchy = 'created_at'


@admin.register(Constraint)
class ConstraintAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'attachment',
        'date',
    )
    list_filter = ('date', 'category')


class NoticeInline(admin.StackedInline):
    model = Notice
    extra = 0


@admin.register(NoticeCategory)
class NoticeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'collapsed'
    )
    list_filter = ('collapsed',)
    inlines = [NoticeInline]
